import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. Configuración de Seguridad y API
# Forzamos el uso de la versión estable 'v1' para evitar el error 404
genai.configure(api_key=st.secrets["GEMINI_API_KEY"], transport='rest')

# 2. Configuración de la página
st.set_page_config(page_title="API GTA - GTAMODE", page_icon="🚗")

st.title("🚗 API GTA")
st.subheader("Transforma tu realidad al estilo Los Santos")
st.write("Sube tus imágenes para activar el **GTAMODE**.")

st.divider()

# 3. Columnas para subir archivos
col1, col2 = st.columns(2)

with col1:
    st.header("1. Entorno Real")
    fondo = st.file_uploader("Sube la foto de la calle o lugar", type=['png', 'jpg', 'jpeg'])
    if fondo:
        st.image(fondo, caption="Fondo seleccionado")

with col2:
    st.header("2. Vehículo GTA")
    vehiculo = st.file_uploader("Sube el auto o moto de GTA", type=['png', 'jpg', 'jpeg'])
    if vehiculo:
        st.image(vehiculo, caption="Vehículo seleccionado")

st.divider()

# 4. Lógica del GTAMODE
if st.button("🚀 ACTIVAR GTAMODE"):
    if fondo and vehiculo:
        with st.spinner("La IA está analizando tu escena estilo San Andreas..."):
            try:
                # Cargar imágenes
                img_fondo = Image.open(fondo)
                img_vehiculo = Image.open(vehiculo)
                
                # Configurar el modelo (usamos gemini-1.5-flash que es el más rápido)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # Instrucción para la IA
                prompt = (
                    "Actúa como un experto en edición de Grand Theft Auto. "
                    "Analiza estas dos imágenes y describe cómo se vería el vehículo de la segunda imagen "
                    "integrado perfectamente en el entorno de la primera. Menciona iluminación, "
                    "estética de GTA y detalles cinematográficos."
                )
                
                # Generar contenido
                response = model.generate_content([prompt, img_fondo, img_vehiculo])
                
                st.success("¡GTAMODE Activado con éxito!")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Hubo un problema técnico: {e}")
    else:
        st.warning("Por favor, asegúrate de subir ambas imágenes antes de activar.")

st.sidebar.write("Desarrollador: Yeison Smit")
