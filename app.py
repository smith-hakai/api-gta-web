import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# Configuración de la página
st.set_page_config(page_title="GTAMODE - Jesmith", layout="centered")

st.title("🎮 GTAMODE ACTIVATED")
st.subheader("Fusiona tu estilo con la estética de GTA")

# Recuperar la API KEY desde los Secrets de Hugging Face
api_key = st.secrets["GEMINI_API_KEY"]

if not api_key:
    st.error("Falta la GEMINI_API_KEY en los Secrets de Settings.")
else:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    col1, col2 = st.columns(2)

    with col1:
        st.write("### 📸 Tu Foto")
        img_persona = st.file_uploader("Sube tu foto aquí", type=['png', 'jpg', 'jpeg'], key="persona")

    with col2:
        st.write("### 🏙️ Fondo de GTA")
        img_fondo = st.file_uploader("Sube el fondo aquí", type=['png', 'jpg', 'jpeg'], key="fondo")

    if img_persona and img_fondo:
        if st.button("🚀 ACTIVAR GTAMODE"):
            with st.spinner("Fusionando estilos..."):
                try:
                    persona_pill = Image.open(img_persona)
                    fondo_pill = Image.open(img_fondo)
                    
                    prompt = """
                    Analiza a la persona en la primera imagen y el escenario en la segunda. 
                    Crea una ilustración digital que fusione a ambos con el estilo artístico de Grand Theft Auto V (estilo Shintani/Rockstar Games). 
                    Usa líneas marcadas, colores saturados y sombras tipo cel-shading. 
                    Mantén la ropa y rasgos de la persona pero adaptados al arte del juego.
                    """
                    
                    response = model.generate_content([prompt, persona_pill, fondo_pill])
                    
                    st.success("¡Resultado generado!")
                    st.write(response.text)
                    # Nota: Gemini 1.5 Flash devuelve texto/descripción. 
                    # Si quieres generación de imagen pura, necesitarías Imagen 3, 
                    # pero por ahora esto validará que tu conexión funciona.
                except Exception as e:
                    st.error(f"Error al procesar: {e}")

st.info("DESARROLLADO POR: JEISON SMITH")
