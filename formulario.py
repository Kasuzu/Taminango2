import streamlit as st
import pandas as pd
import os
import random
from datetime import datetime

# Crear la carpeta 'evidencia' si no existe
if not os.path.exists('evidencia'):
    os.makedirs('evidencia')

# Definir los tips para cada campo con emojis
tips = {
    "nombre": "📝 **Nombre del denunciante:**\nEn esta parte tienes que poner tu nombre. Escribe tu nombre completo, como aparece en tus documentos oficiales. Por ejemplo, si tu nombre es Luis Ángel Martínez Sánchez, escribe 'Luis Ángel Martínez Sánchez'.",
    "genero": "⚥ **Género del denunciante:**\nAquí tienes que seleccionar tu género. Tienes tres opciones: Masculino, Femenino u Otro. Simplemente haz clic en la opción que mejor te describe.",
    "cedula": "🆔 **Cédula del denunciante:**\nEn este espacio, escribe tu número de cédula. La cédula es un número que aparece en tu documento de identidad. Por ejemplo, si tu número de cédula es 987654321, escríbelo exactamente así, sin puntos ni comas.",
    "telefono": "📞 **Teléfono celular del denunciante:**\nAquí tienes que poner tu número de teléfono celular. Asegúrate de escribirlo correctamente para que podamos contactarte si es necesario. Por ejemplo, si tu número es 3219876543, escríbelo sin espacios ni guiones.",
    "email": "📧 **Correo electrónico del denunciante:**\nEn este campo, escribe tu dirección de correo electrónico. Asegúrate de escribirlo correctamente para que podamos enviarte información importante. Por ejemplo, si tu correo es luis.angel@example.com, escríbelo exactamente así.",
    "hecho": "📝 **Descripción del hecho:**\nAquí debes explicar qué ocurrió. Escribe de manera cronológica y detallada lo que pasó, desde el inicio hasta el final. Por ejemplo:\n- Primero, escribe dónde estabas y qué estabas haciendo.\n- Luego, describe lo que sucedió, incluyendo cualquier detalle importante.\n- Finalmente, menciona cómo terminó la situación.\nUn ejemplo podría ser: 'Estaba caminando por el Parque Bolívar en Pasto cuando un hombre se acercó y me robó mi cartera. El hombre era alto y llevaba una chaqueta negra. Después, él corrió hacia la Avenida Colombia y yo llamé a la policía.'",
    "departamento": "🌍 **Departamento:**\nAquí debes escribir el nombre del departamento donde ocurrió el hecho. Por ejemplo, si el hecho ocurrió en Nariño, escribe 'Nariño'.",
    "municipio": "🏙️ **Municipio:**\nEn este campo, escribe el nombre del municipio donde ocurrió el hecho. Por ejemplo, si ocurrió en el municipio de Ipiales, escribe 'Ipiales'.",
    "vereda": "🌾 **Vereda:**\nSi el hecho ocurrió en una vereda, escribe el nombre de la vereda. Por ejemplo, si ocurrió en la vereda 'El Rosario' del municipio de La Cruz, escribe 'El Rosario'. Si no ocurrió en una vereda, puedes dejar este campo en blanco o escribir 'Ninguna'.",
    "implicado": "👤 **Nombre del implicado:**\nAquí debes escribir el nombre de la persona que cometió el delito o que tú crees que cometió el delito. Si no sabes el nombre de la persona, puedes escribir 'Desconocido'. Por ejemplo, si viste a alguien llamado Pedro Gómez cometer el delito, escribe 'Pedro Gómez'.",
    "cedula_implicado": "🆔 **Cédula del implicado:**\nEn este campo, escribe el número de cédula de la persona que cometió el delito, si lo sabes. Si no conoces el número de cédula, puedes escribir 'Desconocido'.",
    "evidencia": "📸 **Subir fotografías o videos:**\nAquí puedes subir cualquier foto o video que tengas como evidencia del hecho. Haz clic en el botón 'Subir' y selecciona los archivos desde tu computadora o dispositivo móvil. Asegúrate de que las fotos o videos estén claros y muestren lo que ocurrió. Por ejemplo, una foto del daño a tu propiedad o un video del incidente en el centro de Pasto puede ser útil."
}

# Inicializar el tip seleccionado en el estado de Streamlit
if 'selected_tip' not in st.session_state:
    st.session_state['selected_tip'] = 'ℹ️ **Instrucciones para llenar el formulario**\nSelecciona un campo y haz clic en "Ayuda" para ver las instrucciones.'

# Función para actualizar el tip seleccionado
def update_tip(tip_key):
    st.session_state['selected_tip'] = tips[tip_key]

# Mostrar el tip actual en la barra lateral
st.sidebar.header("Instrucciones")
st.sidebar.markdown(st.session_state['selected_tip'], unsafe_allow_html=True)

# Título del formulario con emoji
st.title("📄 Formulario de Denuncias Penales - Taminango")

# Información del denunciante
st.header("👤 Información del Denunciante")
anonima = st.checkbox("Denuncia anónima")

if not anonima:
    col1, col2 = st.columns([4, 1])
    with col1:
        nombre = st.text_input("Nombre del denunciante", key="nombre")
    with col2:
        st.button("❓ Ayuda", on_click=update_tip, args=("nombre",), key="ayuda_nombre")

    col1, col2 = st.columns([4, 1])
    with col1:
        genero = st.selectbox("Género", ["Masculino", "Femenino", "Otro"], key="genero")
    with col2:
        st.button("❓ Ayuda", on_click=update_tip, args=("genero",), key="ayuda_genero")

    col1, col2 = st.columns([4, 1])
    with col1:
        cedula = st.text_input("Cédula del denunciante", key="cedula")
    with col2:
        st.button("❓ Ayuda", on_click=update_tip, args=("cedula",), key="ayuda_cedula")

    col1, col2 = st.columns([4, 1])
    with col1:
        telefono = st.text_input("Teléfono celular", key="telefono")
    with col2:
        st.button("❓ Ayuda", on_click=update_tip, args=("telefono",), key="ayuda_telefono")

    col1, col2 = st.columns([4, 1])
    with col1:
        email = st.text_input("Correo electrónico", key="email")
    with col2:
        st.button("❓ Ayuda", on_click=update_tip, args=("email",), key="ayuda_email")
else:
    nombre = "Anónimo"
    genero = "Anónimo"
    cedula = "Anónimo"
    telefono = "Anónimo"
    email = "Anónimo"
    st.text_input("Nombre del denunciante", value=nombre, disabled=True)
    st.selectbox("Género", ["Masculino", "Femenino", "Otro"], index=0, disabled=True)
    st.text_input("Cédula del denunciante", value=cedula, disabled=True)
    st.text_input("Teléfono celular", value=telefono, disabled=True)
    st.text_input("Correo electrónico", value=email, disabled=True)

# Descripción del hecho
col1, col2 = st.columns([4, 1])
with col1:
    hecho = st.text_area("Descripción del hecho", key="hecho")
with col2:
    st.button("❓ Ayuda", on_click=update_tip, args=("hecho",), key="ayuda_hecho")

# Ubicación del hecho
col1, col2 = st.columns([4, 1])
with col1:
    departamento = st.text_input("Departamento", key="departamento")
with col2:
    st.button("❓ Ayuda", on_click=update_tip, args=("departamento",), key="ayuda_departamento")

col1, col2 = st.columns([4, 1])
with col1:
    municipio = st.text_input("Municipio", key="municipio")
with col2:
    st.button("❓ Ayuda", on_click=update_tip, args=("municipio",), key="ayuda_municipio")

col1, col2 = st.columns([4, 1])
with col1:
    vereda = st.text_input("Vereda", key="vereda")
with col2:
    st.button("❓ Ayuda", on_click=update_tip, args=("vereda",), key="ayuda_vereda")

# Información del implicado
st.header("👤 Información del Implicado")
implicados = []
num_implicados = 1
investigar = st.checkbox("No sé quién cometió el delito")

if investigar:
    implicado = "SE DEBE INVESTIGAR"
    cedula_implicado = "SE DEBE INVESTIGAR"
    implicados.append((implicado, cedula_implicado))
    st.text_input("Nombre del implicado", value=implicado, disabled=True)
    st.text_input("Cédula del implicado", value=cedula_implicado, disabled=True)
else:
    while True:
        col1, col2 = st.columns([4, 1])
        with col1:
            implicado = st.text_input("Nombre del implicado", key=f"implicado_{num_implicados}")
        with col2:
            st.button("❓ Ayuda", on_click=update_tip, args=("implicado",), key=f"button_implicado_{num_implicados}")
        
        col1, col2 = st.columns([4, 1])
        with col1:
            cedula_implicado = st.text_input("Cédula del implicado", key=f"cedula_implicado_{num_implicados}")
        with col2:
            st.button("❓ Ayuda", on_click=update_tip, args=("cedula_implicado",), key=f"button_cedula_implicado_{num_implicados}")
        
        if implicado and cedula_implicado:
            implicados.append((implicado, cedula_implicado))
        
        agregar_mas = st.checkbox("Agregar otro implicado", key=f"agregar_{num_implicados}")
        num_implicados += 1
        if not agregar_mas:
            break

# Subida de archivos
col1, col2 = st.columns([4, 1])
with col1:
    fotos_videos = st.file_uploader("Subir fotografías o videos", type=["jpg", "jpeg", "png", "mp4", "mov", "avi"], accept_multiple_files=True)
with col2:
    st.button("❓ Ayuda", on_click=update_tip, args=("evidencia",), key="ayuda_evidencia")

# Verificación de campos obligatorios
if not anonima and (not nombre or not genero or not cedula or not telefono or not email):
    st.error("❗ Todos los campos del denunciante son obligatorios.")
elif not hecho or not departamento or not municipio or not vereda or not implicados:
    st.error("❗ Todos los campos de la denuncia son obligatorios.")
else:
    # Botón para enviar el formulario
    if st.button("📨 Enviar denuncia"):
        # Generar un ID único basado en la fecha y cuatro números aleatorios
        now = datetime.now()
        date_str = now.strftime("%Y%m%d")
        random_digits = random.randint(1000, 9999)
        denuncia_id = f"{date_str}{random_digits}"
        
        evidencia_dir = os.path.join('evidencia', denuncia_id)
        os.makedirs(evidencia_dir)

        # Convertir implicados a un formato de cadena de texto para CSV
        implicados_str = '; '.join([f"{imp[0]} ({imp[1]})" for imp in implicados])

        data = {
            "ID": denuncia_id,
            "Nombre": nombre,
            "Género": genero,
            "Cédula": cedula,
            "Teléfono": telefono,
            "Email": email,
            "Hecho": hecho,
            "Departamento": departamento,
            "Municipio": municipio,
            "Vereda": vereda,
            "Implicados": implicados_str,
            "Fecha": now.strftime("%Y-%m-%d")
        }
        
        # Guardar los datos en un archivo CSV
        df = pd.DataFrame([data])
        if not os.path.isfile("denuncias.csv"):
            df.to_csv("denuncias.csv", index=False)
        else:
            df.to_csv("denuncias.csv", mode='a', header=False, index=False)

        # Guardar las fotos y videos subidos y cambiar el nombre a verde
        for i, file in enumerate(fotos_videos):
            file_name = f"{denuncia_id}_{i+1}{os.path.splitext(file.name)[1]}"
            file_path = os.path.join(evidencia_dir, file_name)
            
            with open(file_path, "wb") as f:
                f.write(file.getbuffer())
            
            st.markdown(f"<span style='color:green'>{file.name} subido exitosamente como {file_name}</span>", unsafe_allow_html=True)

        st.success("✅ Denuncia enviada exitosamente")

