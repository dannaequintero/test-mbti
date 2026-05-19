import streamlit as st

# -------------------------------------------------
# CONFIGURACIÓN
# -------------------------------------------------

st.set_page_config(
    page_title="Test de Compatibilidad de Personalidad",
    layout="centered"
)

# -------------------------------------------------
# ESTILO
# -------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #f5f5f5;
    color: #222222;
}

h1, h2, h3, h4, h5, h6, p, label, div {
    color: #222222 !important;
}

/* CAJA DE RESULTADO */
.caja-resultado {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #dcdcdc;
    margin-top: 20px;
}

/* BOTÓN PERSONALIZADO */
.stButton > button {
    background-color: white;
    color: #222;
    border: 2px solid #222;
    padding: 10px 20px;
    border-radius: 10px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #222;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# TÍTULO
# -------------------------------------------------

st.markdown("""
<h1 style='text-align:center; color:#222;'>
Test de Compatibilidad de Personalidad
</h1>
""", unsafe_allow_html=True)

st.write("Responde las siguientes preguntas para descubrir tu personalidad y celebridades compatibles.")

# -------------------------------------------------
# VARIABLES MBTI
# -------------------------------------------------

I = E = N = S = T = F = J = P = 0

# -------------------------------------------------
# VARIABLES ENNEAGRAM
# -------------------------------------------------

tipo2 = tipo4 = tipo5 = tipo7 = tipo8 = tipo9 = 0

# -------------------------------------------------
# PREGUNTAS
# -------------------------------------------------

st.subheader("Cuestionario de Personalidad")

q1 = st.radio("1. ¿Qué prefieres hacer en tu tiempo libre?", ["Analizar ideas en silencio", "Salir y vivir experiencias"])
q2 = st.radio("2. Las personas te describen como:", ["Reservado y reflexivo", "Energético y expresivo"])
q3 = st.radio("3. Tomas decisiones basándote en:", ["Lógica", "Emociones"])
q4 = st.radio("4. Tu estilo de vida ideal es:", ["Organizado y planeado", "Flexible y espontáneo"])
q5 = st.radio("5. Lo que más te motiva es:", ["Entender y aprender", "Ayudar a los demás"])
q6 = st.radio("6. Te consideras:", ["Creativo y emocional", "Seguro y dominante"])
q7 = st.radio("7. En situaciones sociales sueles:", ["Observar primero", "Participar de inmediato"])
q8 = st.radio("8. Prefieres:", ["Estabilidad y tranquilidad", "Aventura y diversión"])
q9 = st.radio("9. Te inclinas más por:", ["Ideas abstractas", "Hechos concretos"])
q10 = st.radio("10. En un conflicto tú:", ["Evitas la tensión", "Tomas el control"])

# -------------------------------------------------
# BOTÓN
# -------------------------------------------------

if st.button("Ver resultado"):

    # ---------------- MBTI ----------------

    if q1 == "Analizar ideas en silencio":
        I += 1
        tipo5 += 1
    else:
        E += 1
        tipo7 += 1

    if q2 == "Reservado y reflexivo":
        I += 1
        tipo5 += 1
    else:
        E += 1
        tipo7 += 1

    if q3 == "Lógica":
        T += 1
    else:
        F += 1

    if q4 == "Organizado y planeado":
        J += 1
    else:
        P += 1

    if q5 == "Entender y aprender":
        N += 1
        tipo5 += 1
    else:
        F += 1
        tipo2 += 1

    if q6 == "Creativo y emocional":
        F += 1
        tipo4 += 1
    else:
        T += 1
        tipo8 += 1

    if q7 == "Observar primero":
        I += 1
        tipo9 += 1
    else:
        E += 1
        tipo7 += 1

    if q8 == "Estabilidad y tranquilidad":
        J += 1
        tipo9 += 1
    else:
        P += 1
        tipo7 += 1

    if q9 == "Ideas abstractas":
        N += 1
        tipo4 += 1
    else:
        S += 1
        tipo2 += 1

    if q10 == "Evitas la tensión":
        F += 1
        tipo9 += 1
    else:
        T += 1
        tipo8 += 1

    # ---------------- RESULTADO MBTI ----------------

    resultado_mbti = ""
    resultado_mbti += "I" if I >= E else "E"
    resultado_mbti += "N" if N >= S else "S"
    resultado_mbti += "T" if T >= F else "F"
    resultado_mbti += "J" if J >= P else "P"

    # ---------------- ENNEAGRAM ----------------

    eneagramas = {
        "2w3": tipo2,
        "4w5": tipo4,
        "5w6": tipo5,
        "7w6": tipo7,
        "8w7": tipo8,
        "9w1": tipo9
    }

    resultado_eneagrama = max(eneagramas, key=eneagramas.get)

    # ---------------- DESCRIPCIONES ----------------

    descripciones = {
        "INTJ": "Personas estratégicas, analíticas e independientes.",
        "INTP": "Personas lógicas, curiosas y muy analíticas.",
        "ENTJ": "Líderes naturales, decididos y ambiciosos.",
        "ENTP": "Creativos, curiosos y debatientes.",
        "INFJ": "Empáticos y visionarios.",
        "INFP": "Idealistas, creativos y emocionales.",
        "ENFJ": "Líderes empáticos y sociales.",
        "ENFP": "Entusiastas y creativos.",
        "ISTJ": "Responsables y organizados.",
        "ISFJ": "Leales y cuidadosos.",
        "ESTJ": "Prácticos y directos.",
        "ESFJ": "Sociales y cooperativos.",
        "ISTP": "Observadores y prácticos.",
        "ISFP": "Artísticos y tranquilos.",
        "ESTP": "Energéticos y audaces.",
        "ESFP": "Extrovertidos y divertidos."
    }

    # ---------------- CELEBRIDADES ----------------

    celebridades = {
        "INTJ": ["Elon Musk", "Mark Zuckerberg"],
        "INTP": ["Albert Einstein", "Bill Gates"],
        "ENTJ": ["Steve Jobs", "Gordon Ramsay"],
        "ENTP": ["Robert Downey Jr.", "Tom Hanks"],
        "INFJ": ["Lady Gaga", "Nelson Mandela"],
        "INFP": ["Johnny Depp", "J.K. Rowling"],
        "ENFJ": ["Barack Obama", "Oprah Winfrey"],
        "ENFP": ["Will Smith", "Robin Williams"],
        "ISTJ": ["Jeff Bezos", "Natalie Portman"],
        "ISFJ": ["Beyoncé", "Kate Middleton"],
        "ESTJ": ["Emma Watson", "Hillary Clinton"],
        "ESFJ": ["Taylor Swift", "Steve Harvey"],
        "ISTP": ["Bruce Lee", "Michael Jordan"],
        "ISFP": ["Michael Jackson", "Frida Kahlo"],
        "ESTP": ["Madonna", "Ernest Hemingway"],
        "ESFP": ["Adele", "Marilyn Monroe"]
    }

    # ---------------- RESULTADO ----------------

    st.markdown("### Resultado")

    st.markdown(f"""
    <div class="caja-resultado">
        <h3>Tu MBTI es: {resultado_mbti}</h3>
        <h3>Tu Eneagrama es: {resultado_eneagrama}</h3>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- DESCRIPCIÓN ----------------

    st.subheader("Descripción de tu personalidad")
    st.write(descripciones[resultado_mbti])

    # ---------------- CELEBRIDADES ----------------

    st.subheader("Celebridades compatibles")

    for c in celebridades[resultado_mbti]:
        st.write(f"- {c}")
