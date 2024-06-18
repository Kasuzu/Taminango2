import streamlit as st

def main():
    st.sidebar.title("Navegador")
    option = st.sidebar.selectbox("Seleccione una opción", ("Inicio", "Formulario", "Gráficos"))

    if option == "Inicio":
        show_home()
    elif option == "Formulario":
        st.write("Cargando formulario de denuncia...")
        run_formulario()
    elif option == "Gráficos":
        st.write("Cargando gráficos de denuncias...")
        run_graficos()

def show_home():
    st.title("Sistema de Gestión de Denuncias Penales")
    st.markdown("""
    ## Bienvenido
    Este sistema le permite realizar y visualizar denuncias penales de manera fácil y rápida. Seleccione una opción en el menú de la izquierda para empezar.
    
    ### Opciones disponibles:
    - **Formulario**: Llene el formulario para realizar una nueva denuncia.
    - **Gráficos**: Vea los gráficos de las denuncias realizadas (requiere autenticación).
    """)

def run_formulario():
    with open('formulario.py', encoding='utf-8') as f:
        code = compile(f.read(), 'formulario.py', 'exec')
        exec(code, globals())

def run_graficos():
    if check_password():
        with open('graficos.py', encoding='utf-8') as f:
            code = compile(f.read(), 'graficos.py', 'exec')
            exec(code, globals())

def check_password():
    def password_entered():
        if st.session_state["username"] == "admin" and st.session_state["password"] == "password123":
            st.session_state["authenticated"] = True
        else:
            st.session_state["authenticated"] = False

    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        st.text_input("Nombre de usuario", key="username")
        st.text_input("Contraseña", type="password", key="password")
        st.button("Iniciar sesión", on_click=password_entered)
        if st.session_state["authenticated"] == False:
            st.error("Nombre de usuario o contraseña incorrectos")
        return False
    else:
        return True

if __name__ == "__main__":
    main()
