import streamlit as st

st.title("👋 Hello, Streamlit!")
st.write("¡Bienvenido a tu primera app web con Python!")

nombre = st.text_input("¿Cómo te llamás?")
if nombre:
    st.success(f"¡Encantado de conocerte, {nombre}!")

st.write("Probá el siguiente control deslizante:")
valor = st.slider("Elegí un número", 0, 100, 50)
st.write(f"Valor seleccionado: {valor}")
