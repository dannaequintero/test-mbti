import streamlit as st

st.set_page_config(page_title="MBTI Test", page_icon="🧠", layout="centered")

# 🌌 Fondo + estilo PRO
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: white;
    }

    h1, h2, h3, p {
        color: white !important;
    }

    .card {
        background-color: rgba(255,255,255,0.08);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎨 Título
st.markdown(
    "<h1 style='text-align: center;'>🧠 Test de Personalidad MBTI</h1>",
    unsafe_allow_html=True
)

st.write("Descubre tu tipo de personalidad y celebridades similares ✨")

# 👑 Celebridades con imágenes
celebridades = {
    "INTJ": [
        {"nombre": "Elon Musk", "img": "https://upload.wikimedia.org/wikipedia/commons/e/ed/Elon_Musk_Royal_Society_%28crop1%29.jpg"},
        {"nombre": "Mark Zuckerberg", "img": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Mark_Zuckerberg_F8_2019_Keynote_%28cropped%29.jpg"},
        {"nombre": "Isaac Newton", "img": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Sir_Isaac_Newton_%281643-1727%29.jpg"}
    ],
    "ENTP": [
        {"nombre": "Robert Downey Jr.", "img": "https://upload.wikimedia.org/wikipedia/commons/5/5c/Robert_Downey_Jr_2014_Comic_Con.jpg"},
        {"nombre": "Tom Hanks", "img": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Tom_Hanks_TIFF_2019.jpg"},
        {"nombre": "Sacha Baron Cohen", "img": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Sacha_Baron_Cohen_2019.jpg"}
    ]
}

# 🧠 Descripciones
descripciones = {
    "INTJ": "Personas estratégicas, independientes y analíticas. Les gusta planear a largo plazo.",
    "ENTP": "Creativos, curiosos y debatidores naturales. Aman explorar ideas nuevas."
}

# Variables
I = E = N = S = T = F = J = P = 0

st.markdown("## 📝 Responde las preguntas")

# 👥 I vs E
q1 = st.radio("1. ¿Prefieres pasar tiempo?", ["Solo", "Con otras personas"])
q2 = st.radio("2. Después de socializar te sientes:", ["Cansado", "Con energía"])
q3 = st.radio("3. En una fiesta eres:", ["Reservado", "Sociable"])
q4 = st.radio("4. Prefieres trabajar:", ["Solo", "En equipo"])

# 🧠 S vs N
q5 = st.radio("5. Prefieres:", ["Hechos concretos", "Ideas abstractas"])
q6 = st.radio("6. Te enfocas más en:", ["El presente", "El futuro"])
q7 = st.radio("7. Te gustan más:", ["Instrucciones claras", "Conceptos generales"])
q8 = st.radio("8. Confías más en:", ["Experiencia", "Intuición"])

# ⚖️ T vs F
q9 = st.radio("9. Tomas decisiones con:", ["Lógica", "Emociones"])
q10 = st.radio("10. Valoras más:", ["Justicia", "Empatía"])
q11 = st.radio("11. Eres más:", ["Objetivo", "Comprensivo"])
q12 = st.radio("12. En un conflicto:", ["Analizas", "Sientes"])

# 📅 J vs P
q13 = st.radio("13. Prefieres:", ["Planificar", "Improvisar"])
q14 = st.radio("14. Tu estilo es:", ["Organizado", "Flexible"])
q15 = st.radio("15. Trabajas mejor:", ["Con estructura", "Sin reglas"])
q16 = st.radio("16. Prefieres terminar:", ["Antes", "Al último momento"])

# 🎯 Resultado
if st.button("✨ Ver resultado"):

    I = E = N = S = T = F = J = P = 0

    # lógica
    if q1 == "Solo": I += 1
    else: E += 1

    if q2 == "Cansado": I += 1
    else: E += 1

    if q3 == "Reservado": I += 1
    else: E += 1

    if q4 == "Solo": I += 1
    else: E += 1

    if q5 == "Hechos concretos": S += 1
    else: N += 1

    if q6 == "El presente": S += 1
    else: N += 1

    if q7 == "Instrucciones claras": S += 1
    else: N += 1

    if q8 == "Experiencia": S += 1
    else: N += 1

    if q9 == "Lógica": T += 1
    else: F += 1

    if q10 == "Justicia": T += 1
    else: F += 1

    if q11 == "Objetivo": T += 1
    else: F += 1

    if q12 == "Analizas": T += 1
    else: F += 1

    if q13 == "Planificar": J += 1
    else: P += 1

    if q14 == "Organizado": J += 1
    else: P += 1

    if q15 == "Con estructura": J += 1
    else: P += 1

    if q16 == "Antes": J += 1
    else: P += 1

    # resultado
    resultado = ""
    resultado += "I" if I >= E else "E"
    resultado += "N" if N >= S else "S"
    resultado += "T" if T >= F else "F"
    resultado += "J" if J >= P else "P"

    # tarjeta resultado
    st.markdown(
        f"""
        <div class='card'>
            <h2>🧠 Tu tipo de personalidad es: {resultado}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    # descripción
    if resultado in descripciones:
        st.markdown("### 🧠 Descripción psicográfica:")
        st.write(descripciones[resultado])

    # celebridades
    if resultado in celebridades:
        st.markdown("### ✨ Celebridades con tu tipo:")

        cols = st.columns(3)

        for i, persona in enumerate(celebridades[resultado]):
            with cols[i % 3]:
                st.markdown("<div class='card'>", unsafe_allow_html=True)
                st.image(persona["img"], use_container_width=True)
                st.markdown(f"**{persona['nombre']}**")
                st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.info("Basado en análisis de datos del modelo MBTI.")
