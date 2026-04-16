import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuración directa y simple
# Usamos el método más estable de conexión
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
        with st.spinner("La IA está analizando la escena..."):
            try:
                # Cargamos las imágenes
                img_fondo = Image.open(fondo)
                img_vehiculo = Image.open(vehiculo)
                
                # LLAMADA DIRECTA AL MODELO ESTABLE
                # Eliminamos 'models/' del nombre para ver si tu entorno lo prefiere así
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = "Fusiona estas imágenes al estilo GTA San Andreas. Describe la escena final."
                
                # Generamos el contenido
                response = model.generate_content([prompt, img_fondo, img_vehiculo])
                
                st.success("¡GTAMODE Activado!")
                st.write(response.text)
                
            except Exception as e:
                # Si falla, intentamos con el nombre alternativo automáticamente
                try:
                    model_alt = genai.GenerativeModel('gemini-pro-vision')
                    response = model_alt.generate_content([prompt, img_fondo, img_vehiculo])
                    st.success("¡GTAMODE Activado (vía backup)!")
                    st.write(response.text)
                except:
                    st.error(f"Error persistente: {e}")
    else:
        st.warning("Sube ambas imágenes.")

st.sidebar.write("Desarrollador: Jeison Smith")
