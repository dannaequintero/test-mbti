import streamlit as st
import pandas as pd
import numpy as np

# -------------------------------------------------
# CONFIGURACIÓN
# -------------------------------------------------

st.set_page_config(
    page_title="Test de Compatibilidad de Personalidad",
    page_icon="🧠",
    layout="centered"
)

st.title("Test de Compatibilidad de Personalidad")
st.write("Responde las 16 preguntas para obtener tu MBTI y compatibilidad.")

# -------------------------------------------------
# CARGAR CSV
# -------------------------------------------------

df = pd.read_csv("celebridades_mbti.csv")

# -------------------------------------------------
# VECTOR MBTI
# -------------------------------------------------

mbti_to_vec = {
    "INTJ":[1,0,1,0],
    "INTP":[1,0,1,1],
    "ENTJ":[0,1,1,0],
    "ENTP":[0,1,1,1],
    "INFJ":[1,0,0,0],
    "INFP":[1,0,0,1],
    "ENFJ":[0,1,0,0],
    "ENFP":[0,1,0,1],
    "ISTJ":[1,0,1,0],
    "ISFJ":[1,0,0,0],
    "ESTJ":[0,1,1,0],
    "ESFJ":[0,1,0,0],
    "ISTP":[1,0,1,1],
    "ISFP":[1,0,0,1],
    "ESTP":[0,1,1,1],
    "ESFP":[0,1,0,1]
}

# -------------------------------------------------
# COSINE SIMILARITY
# -------------------------------------------------

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# -------------------------------------------------
# PREGUNTAS (16)
# -------------------------------------------------

st.subheader("Cuestionario")

# E vs I
q1 = st.radio("1. Prefieres:", ["Solo", "Con gente"])
q2 = st.radio("2. Te recargas con:", ["Soledad", "Socializar"])
q3 = st.radio("3. En eventos eres:", ["Observador", "Participativo"])
q4 = st.radio("4. Prefieres trabajar:", ["Individual", "Equipo"])

# S vs N
q5 = st.radio("5. Prefieres:", ["Hechos", "Ideas"])
q6 = st.radio("6. Te enfocas en:", ["Presente", "Futuro"])
q7 = st.radio("7. Confías en:", ["Experiencia", "Intuición"])
q8 = st.radio("8. Aprendes mejor con:", ["Ejemplos", "Conceptos"])

# T vs F
q9 = st.radio("9. Decides con:", ["Lógica", "Emoción"])
q10 = st.radio("10. Valoras:", ["Justicia", "Empatía"])
q11 = st.radio("11. Eres más:", ["Objetivo", "Comprensivo"])
q12 = st.radio("12. En conflictos:", ["Analizas", "Sientes"])

# J vs P
q13 = st.radio("13. Prefieres:", ["Planificar", "Improvisar"])
q14 = st.radio("14. Estilo de vida:", ["Organizado", "Flexible"])
q15 = st.radio("15. Trabajas mejor:", ["Con estructura", "Sin estructura"])
q16 = st.radio("16. Prefieres terminar:", ["Antes", "Último momento"])

# -------------------------------------------------
# BOTÓN RESULTADO
# -------------------------------------------------

if st.button("Ver resultado"):

    # ---------------- MBTI ----------------

    I = E = N = S = T = F = J = P = 0

    # E/I
    if q1 == "Solo": I += 1
    else: E += 1
    if q2 == "Soledad": I += 1
    else: E += 1
    if q3 == "Observador": I += 1
    else: E += 1
    if q4 == "Individual": I += 1
    else: E += 1

    # S/N
    if q5 == "Hechos": S += 1
    else: N += 1
    if q6 == "Presente": S += 1
    else: N += 1
    if q7 == "Experiencia": S += 1
    else: N += 1
    if q8 == "Ejemplos": S += 1
    else: N += 1

    # T/F
    if q9 == "Lógica": T += 1
    else: F += 1
    if q10 == "Justicia": T += 1
    else: F += 1
    if q11 == "Objetivo": T += 1
    else: F += 1
    if q12 == "Analizas": T += 1
    else: F += 1

    # J/P
    if q13 == "Planificar": J += 1
    else: P += 1
    if q14 == "Organizado": J += 1
    else: P += 1
    if q15 == "Con estructura": J += 1
    else: P += 1
    if q16 == "Antes": J += 1
    else: P += 1

    resultado_mbti = ""
    resultado_mbti += "I" if I >= E else "E"
    resultado_mbti += "N" if N >= S else "S"
    resultado_mbti += "T" if T >= F else "F"
    resultado_mbti += "J" if J >= P else "P"

    st.success(f"Tu tipo MBTI es: {resultado_mbti}")

    # -------------------------------------------------
# DESCRIPCIÓN DE PERSONALIDAD
# -------------------------------------------------

descripciones = {
    "INTJ": "Personas estratégicas, analíticas y muy independientes.",
    "INTP": "Lógicos, curiosos y amantes del conocimiento.",
    "ENTJ": "Líderes naturales, organizados y decididos.",
    "ENTP": "Creativos, debatientes y muy innovadores.",
    "INFJ": "Empáticos, profundos y visionarios.",
    "INFP": "Idealistas, sensibles y guiados por valores.",
    "ENFJ": "Líderes sociales, empáticos y motivadores.",
    "ENFP": "Entusiastas, creativos y sociables.",
    "ISTJ": "Responsables, estructurados y confiables.",
    "ISFJ": "Protectores, leales y detallistas.",
    "ESTJ": "Prácticos, directos y organizados.",
    "ESFJ": "Sociales, amables y cooperativos.",
    "ISTP": "Observadores, prácticos y resolutivos.",
    "ISFP": "Artísticos, tranquilos y sensibles.",
    "ESTP": "Energéticos, espontáneos y arriesgados.",
    "ESFP": "Extrovertidos, divertidos y expresivos."
}

st.subheader("Tu personalidad")
st.write(descripciones.get(resultado_mbti, "Perfil no encontrado"))
    
    # -------------------------------------------------
    # SIMILITUD
    # -------------------------------------------------

    usuario_vec = mbti_to_vec.get(resultado_mbti, [0,0,0,0])

    df["vector"] = df["mbti"].apply(lambda x: mbti_to_vec.get(x, [0,0,0,0]))

    df["compatibilidad"] = df["vector"].apply(
        lambda v: cosine_similarity(usuario_vec, v)
    ) * 100

    # -------------------------------------------------
    # TOP RESULTADOS
    # -------------------------------------------------

    st.subheader("Top celebridades compatibles")

    top = df.sort_values("compatibilidad", ascending=False).head(5)

    for _, row in top.iterrows():
        st.write(f"⭐ {row['nombre']} - {row['compatibilidad']:.1f}%")

    st.markdown("---")
    st.info("Sistema basado en similitud de personalidad MBTI.")
