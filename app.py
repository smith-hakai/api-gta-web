
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="API GTA - GTAMODE", page_icon="🚗")

# Estilo visual
st.title("🚗 API GTA")
st.subheader("Transforma tu realidad al estilo Los Santos")
st.write("Sube tus imágenes para activar el **GTAMODE**.")

st.divider()

# Columnas para subir archivos
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

# Botón de acción
if st.button("🚀 ACTIVAR GTAMODE"):
    if fondo and vehiculo:
        st.info("Conectando con la API... Preparando tu imagen con estilo San Andreas.")
        # Aquí irá la lógica de conexión que configuraremos después
    else:
        st.warning("Por favor, sube ambas imágenes para continuar.")

st.sidebar.title("Configuración")
st.sidebar.write("Proyecto: API GTA")
st.sidebar.write("Desarrollador: Yeison Smit")
