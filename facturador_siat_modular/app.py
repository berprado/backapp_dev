import streamlit as st
from utils import setup_logging # Importamos la función

# Llamamos a setup_logging() lo antes posible para configurar el logger
# Es importante que esto se ejecute solo una vez.
# Streamlit puede re-ejecutar el script en ciertas interacciones.
# Una forma de asegurar que solo se ejecute una vez es verificar si ya se configuró,
# o confiar en que la propia función setup_logging maneja múltiples llamadas (como lo hace la nuestra).
setup_logging()

def main():
    st.set_page_config(
        page_title="Facturador SIAT Modular",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("Bienvenido al Facturador SIAT Modular")
    st.write("Seleccione una opción del menú lateral para comenzar.")

    # Aquí se podrían añadir dashboards o información general

if __name__ == "__main__":
    main()
