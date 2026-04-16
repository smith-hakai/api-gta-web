import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuración de la API Key desde los Secrets de Streamlit
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

st.set_page_config(page_title="API GTA - GTAMODE", page_icon="🚗")

st.title("🚗 API GTA")
st.subheader("Transforma tu realidad al estilo Los Santos")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header("1. Entorno Real")
    fondo = st.file_uploader("Sube la foto del lugar", type=['png', 'jpg', 'jpeg'])
    if fondo:
        st.image(fondo, caption="Fondo seleccionado")

with col2:
    st.header("2. Vehículo GTA")
    vehiculo = st.file_uploader("Sube el auto o moto de GTA", type=['png', 'jpg', 'jpeg'])
    if vehiculo:
        st.image(vehiculo, caption="Vehículo seleccionado")

st.divider()

if st.button("🚀 ACTIVAR GTAMODE"):
    if fondo and vehiculo:
        with st.spinner("Fusionando imágenes con estilo San Andreas..."):
            try:
                # Cargamos las imágenes
                img_fondo = Image.open(fondo)
                img_vehiculo = Image.open(vehiculo)
                
                # Configuramos el modelo
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # Instrucción para la IA
                prompt = (
                    "Analiza estas dos imágenes. La primera es un entorno real y la segunda es un vehículo de GTA. "
                    "Describe detalladamente cómo se vería el vehículo integrado en ese entorno real, "
                    "ajustando la iluminación, sombras y el estilo visual para que parezca una captura de GTA VI."
                )
                
                # Generamos la respuesta
                response = model.generate_content([prompt, img_fondo, img_vehiculo])
                
                st.success("¡Análisis de GTAMODE completado!")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Error al conectar con la IA: {e}")
    else:
        st.warning("Faltan imágenes para procesar.")

st.sidebar.write("Desarrollador: Yeison Smit")
