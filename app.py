import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# 1. Ajuste de compatibilidad (Forzar versión estable v1)
os.environ["GOOGLE_API_USE_MTLS"] = "never" 

# 2. Configuración de la API Key
# Se conecta con la llave que guardaste en los Secrets de Streamlit
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 3. Configuración visual de la página
st.set_page_config(page_title="API GTA - GTAMODE", page_icon="🚗")

st.title("🚗 API GTA")
st.subheader("Transforma tu realidad al estilo Los Santos")
st.write("Sube tus imágenes para activar el **GTAMODE**.")

st.divider()

# 4. Interfaz para subir archivos
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

# 5. Botón de acción y lógica de IA
if st.button("🚀 ACTIVAR GTAMODE"):
    if fondo and vehiculo:
        with st.spinner("La IA está analizando la escena..."):
            try:
                # Cargar las imágenes enviadas por el usuario
                img_fondo = Image.open(fondo)
                img_vehiculo = Image.open(vehiculo)
                
                # Definir el modelo usando la ruta completa para evitar el error 404
                model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
                
                # Instrucciones precisas para la IA
                prompt = (
                    "Actúa como un motor de renderizado de GTA. "
                    "Toma el vehículo de la segunda imagen y colócalo en el entorno de la primera. "
                    "Describe detalladamente cómo se vería la escena: sombras, reflejos "
                    "y el acabado estético de Grand Theft Auto."
                )
                
                # Enviar a Google para procesar
                response = model.generate_content([prompt, img_fondo, img_vehiculo])
                
                st.success("¡GTAMODE Activado!")
                st.write(response.text)
                
            except Exception as e:
                # Si algo falla, aquí veremos el detalle exacto
                st.error(f"Hubo un problema técnico: {e}")
    else:
        st.warning("Debes subir ambas imágenes primero.")

st.sidebar.write("Desarrollador: Jeison Smith")
