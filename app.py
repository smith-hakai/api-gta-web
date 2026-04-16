
import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# Configuración visual de la página
st.set_page_config(page_title="GTAMODE - Jesmith", layout="centered")

st.title("🎮 GTAMODE ACTIVATED")
st.subheader("Integra vehículos de Los Santos en ciudades reales")

# Recuperar la API KEY desde los Secrets (Docker/HuggingFace)
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except:
    api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("⚠️ Falta la GEMINI_API_KEY en los Secrets de Settings.")
else:
    # Configuración del modelo
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Diseño de dos columnas para las subidas
    col1, col2 = st.columns(2)

    with col1:
        st.write("### 🚗 VEHÍCULO GTA")
        img_vehiculo = st.file_uploader("Sube el coche o moto estilo GTA", type=['png', 'jpg', 'jpeg'], key="vehiculo")

    with col2:
        st.write("### 🏙️ CIUDAD REAL")
        img_ciudad = st.file_uploader("Sube la foto de la calle o ciudad", type=['png', 'jpg', 'jpeg'], key="ciudad")

    st.markdown("---")

    # Botón principal siempre visible
    if st.button("🚀 LANZAR FUSIÓN GTAMODE", use_container_width=True):
        if img_vehiculo and img_ciudad:
            with st.spinner("Procesando integración..."):
                try:
                    vehiculo_pill = Image.open(img_vehiculo)
                    ciudad_pill = Image.open(img_ciudad)
                    
                    # Prompt específico para tu visión del proyecto
                    prompt = """
                    Actúa como un experto en edición visual de Rockstar Games. 
                    Toma el vehículo de la primera imagen (estilo artístico GTA) e intégralo 
                    perfectamente en la escena de la ciudad real de la segunda imagen. 
                    El vehículo debe mantener su estilo de dibujo/ilustración, pero debe 
                    estar posicionado sobre el pavimento con sombras coherentes. 
                    Describe el resultado o genera la visión de esta fusión.
                    """
                    
                    response = model.generate_content([prompt, vehiculo_pill, ciudad_pill])
                    
                    st.success("¡GTAMODE Completado!")
                    st.write(response.text)
                    
                except Exception as e:
                    st.error(f"Error técnico: {e}")
        else:
            st.warning("⚠️ Debes subir ambas imágenes para ejecutar el GTAMODE.")

# Pie de página
st.markdown("<br><br>", unsafe_allow_html=True)
st.info("DESARROLLADO POR: JEISON SMITH")
