import streamlit as st
import pandas as pd

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

.caja-resultado {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #dcdcdc;
    margin-top: 20px;
}

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
# CARGAR DATASET (CSV desde GitHub)
# -------------------------------------------------

df = pd.read_csv("celebridades_mbti.csv")

# -------------------------------------------------
# TÍTULO
# -------------------------------------------------

st.markdown("""
<h1 style='text-align:center; color:#222;'>
Test de Compatibilidad de Personalidad
</h1>
""", unsafe_allow_html=True)

st.write("Responde las preguntas para descubrir tu personalidad y compatibilidad.")

# -------------------------------------------------
# VARIABLES
# -------------------------------------------------

I = E = N = S = T = F = J = P = 0
tipo2 = tipo4 = tipo5 = tipo7 = tipo8 = tipo9 = 0

# -------------------------------------------------
# PREGUNTAS
# -------------------------------------------------

st.subheader("Cuestionario")

q1 = st.radio("1. ¿Qué prefieres?", ["Analizar ideas en silencio", "Salir y vivir experiencias"])
q2 = st.radio("2. Te describen como:", ["Reservado", "Energético"])
q3 = st.radio("3. Decides con:", ["Lógica", "Emociones"])
q4 = st.radio("4. Prefieres:", ["Planificado", "Espontáneo"])
q5 = st.radio("5. Te motiva:", ["Conocimiento", "Ayudar a otros"])
q6 = st.radio("6. Eres:", ["Creativo y emocional", "Seguro y dominante"])
q7 = st.radio("7. En social:", ["Observo primero", "Participo rápido"])
q8 = st.radio("8. Prefieres:", ["Tranquilidad", "Aventura"])
q9 = st.radio("9. Te inclinas a:", ["Ideas abstractas", "Hechos concretos"])
q10 = st.radio("10. En conflicto:", ["Evito tensión", "Tomo control"])

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

    if q2 == "Reservado":
        I += 1
        tipo5 += 1
    else:
        E += 1
        tipo7 += 1

    if q3 == "Lógica":
        T += 1
    else:
        F += 1

    if q4 == "Planificado":
        J += 1
    else:
        P += 1

    if q5 == "Conocimiento":
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

    if q7 == "Observo primero":
        I += 1
        tipo9 += 1
    else:
        E += 1
        tipo7 += 1

    if q8 == "Tranquilidad":
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

    if q10 == "Evito tensión":
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

    eneagrama = {
        "2w3": tipo2,
        "4w5": tipo4,
        "5w6": tipo5,
        "7w6": tipo7,
        "8w7": tipo8,
        "9w1": tipo9
    }

    resultado_eneagrama = max(eneagrama, key=eneagrama.get)

    # ---------------- RESULTADO UI ----------------

    st.markdown("### Resultado")

    st.markdown(f"""
    <div class="caja-resultado">
        <h3>MBTI: {resultado_mbti}</h3>
        <h3>Eneagrama: {resultado_eneagrama}</h3>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- DESCRIPCIÓN ----------------

    st.subheader("Descripción")

    descripciones = {
        "INTJ": "Personas estratégicas y analíticas.",
        "INTP": "Lógicas y curiosas.",
        "ENTJ": "Líderes naturales.",
        "ENTP": "Creativos y debatientes.",
        "INFJ": "Empáticos y visionarios.",
        "INFP": "Idealistas y emocionales.",
        "ENFJ": "Líderes sociales.",
        "ENFP": "Entusiastas.",
        "ISTJ": "Organizados y responsables.",
        "ISFJ": "Leales y cuidadosos.",
        "ESTJ": "Prácticos y directos.",
        "ESFJ": "Sociales y cooperativos.",
        "ISTP": "Observadores.",
        "ISFP": "Artísticos.",
        "ESTP": "Energéticos.",
        "ESFP": "Extrovertidos."
    }

    st.write(descripciones.get(resultado_mbti, "Perfil mixto."))

    # ---------------- CELEBRIDADES DESDE CSV ----------------

    st.subheader("Celebridades compatibles")

    resultados = df[df["mbti"] == resultado_mbti]

    for _, row in resultados.iterrows():
        st.write(f"- {row['nombre']} ({row['ocupacion']})")
