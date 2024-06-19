import streamlit as st
import base64
from PIL import Image

def main():
    # Cargar las imágenes
    background_image = 'FONDOTAM.png'
    header_image = 'ENCABEZADO.png'
    footer_image = 'PIE.png'

    # Aplicar estilo para fondo
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{get_base64_of_bin_file(background_image)}");
        background-size: cover;
        background-position: center;
    }}
    [data-testid="stHeader"] {{
        display: none;
    }}
    [data-testid="stSidebar"] {{
        background: rgba(255, 255, 255, 0.8);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Mostrar encabezado
    st.image(header_image, use_column_width=True)

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

    # Mostrar pie de página
    st.image(footer_image, use_column_width=True)

def show_home():
    st.title("Sistema de Gestión de Denuncias y Quejas en el Municipio de Taminango, Nariño")
    st.markdown("""
    ## Bienvenido/a

    🎉 ¡Bienvenido/a al Sistema de Gestión de Denuncias y Quejas en el Municipio de Taminango, Nariño! 🎉

    Este sistema le permite realizar y visualizar denuncias penales y quejas de manera fácil y rápida. Siga las instrucciones a continuación para utilizar la plataforma de manera efectiva.
    """)

    with st.expander("📄 **Formulario**"):
        st.markdown("""
        ### Realizar una Denuncia o Queja
        - Para realizar una denuncia o queja, seleccione la opción **Formulario** del menú.
        - Una vez seleccionado, verá un formulario con varios campos que debe llenar con la información relevante sobre la denuncia o queja.

        #### **Campos del Formulario**:
        1. **👤 Denuncia Anónima**:
           - Marque esta casilla si desea que su denuncia o queja sea anónima. Si selecciona esta opción, los campos de información personal se desactivarán automáticamente.

        2. **📝 Nombre del Denunciante**:
           - Escriba su nombre completo como aparece en sus documentos oficiales.

        3. **⚥ Género del Denunciante**:
           - Seleccione su género: Masculino, Femenino u Otro.

        4. **🆔 Cédula del Denunciante**:
           - Ingrese su número de cédula sin puntos ni comas.

        5. **📞 Teléfono Celular del Denunciante**:
           - Escriba su número de teléfono celular para que podamos contactarlo si es necesario.

        6. **📧 Correo Electrónico del Denunciante**:
           - Proporcione su dirección de correo electrónico para recibir notificaciones importantes.

        7. **📝 Descripción del Hecho**:
           - Explique detalladamente y de manera cronológica lo que ocurrió. Incluya todos los detalles importantes.

        8. **🌍 Ubicación del Hecho**:
           - **Departamento**: Ingrese el nombre del departamento donde ocurrió el hecho.
           - **Municipio**: Escriba el nombre del municipio donde ocurrió el hecho.
           - **Vereda**: Si el hecho ocurrió en una vereda, indique el nombre de la vereda. Si no, escriba 'Ninguna'.

        9. **👤 Información del Implicado**:
           - **Nombre del Implicado**: Ingrese el nombre de la persona que cometió el delito o la queja. Si no conoce el nombre, escriba 'Desconocido'.
           - **🆔 Cédula del Implicado**: Ingrese la cédula del implicado si la conoce. De lo contrario, escriba 'Desconocido'.
           - Marque la casilla "No sé quién cometió el delito" si no sabe quién es el implicado, y se llenará automáticamente con 'SE DEBE INVESTIGAR'.

        10. **📸 Subir Fotografías o Videos**:
            - Puede subir fotos o videos como evidencia del hecho. Haga clic en el botón 'Subir' y seleccione los archivos desde su dispositivo.

        11. **📨 Enviar Denuncia**:
            - Revise que todos los campos estén correctamente llenados. Luego, haga clic en el botón "Enviar denuncia". Una vez enviada, recibirá una confirmación de que la denuncia se ha registrado correctamente.
        """)

    with st.expander("📊 **Gráficos**"):
        st.markdown("""
        ### Visualizar Denuncias y Quejas (Requiere Autenticación)
        - Para visualizar las denuncias y quejas realizadas, seleccione la opción **Gráficos** en el menú.
        - Deberá autenticarse proporcionando un nombre de usuario y una contraseña.

        #### **Visualización de Datos**:
        1. **Filtros**:
           - Utilice los filtros en el panel lateral para seleccionar los datos que desea visualizar. Puede filtrar por municipios, géneros y un rango de fechas.

        2. **Gráficos de Denuncias y Quejas**:
           - **Distribución por Género**: Vea la cantidad de denuncias y quejas realizadas por cada género.
           - **Distribución por Municipio**: Observe la cantidad de denuncias y quejas por municipio.
           - **Nube de Palabras**: Visualice los términos más frecuentes en las descripciones de los hechos denunciados.
           - **Frecuencia de Denuncias Anónimas vs. No Anónimas**: Compare la cantidad de denuncias anónimas con las no anónimas.
           - **Distribución por Vereda**: Vea la cantidad de denuncias y quejas por vereda.

        3. **Exportación de Datos**:
           - Puede exportar los datos filtrados a un archivo CSV para un análisis más detallado haciendo clic en el botón "📥 Descargar Datos Filtrados".

        4. **Búsqueda de Caso por Palabra Clave**:
           - Ingrese una palabra clave para buscar casos específicos. Se mostrarán los ID de los casos y los hechos asociados.

        5. **Descarga de Evidencias**:
           - Seleccione un ID de denuncia o queja para ver si hay evidencias disponibles. Puede buscar y descargar las evidencias asociadas a un caso específico.
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

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

if __name__ == "__main__":
    main()
