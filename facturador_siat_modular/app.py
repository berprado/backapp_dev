import streamlit as st

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
