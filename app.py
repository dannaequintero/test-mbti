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

# -------------------------------------------------
# CARGA CSV
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
# PREGUNTAS MBTI (16)
# -------------------------------------------------

st.subheader("Cuestionario MBTI")

q1 = st.radio("1. Prefieres:", ["Solo", "Con gente"])
q2 = st.radio("2. Te recargas con:", ["Soledad", "Socializar"])
q3 = st.radio("3. En eventos eres:", ["Observador", "Participativo"])
q4 = st.radio("4. Prefieres trabajar:", ["Individual", "Equipo"])

q5 = st.radio("5. Prefieres:", ["Hechos", "Ideas"])
q6 = st.radio("6. Te enfocas en:", ["Presente", "Futuro"])
q7 = st.radio("7. Confías en:", ["Experiencia", "Intuición"])
q8 = st.radio("8. Aprendes mejor con:", ["Ejemplos", "Conceptos"])

q9 = st.radio("9. Decides con:", ["Lógica", "Emoción"])
q10 = st.radio("10. Valoras:", ["Justicia", "Empatía"])
q11 = st.radio("11. Eres más:", ["Objetivo", "Comprensivo"])
q12 = st.radio("12. En conflictos:", ["Analizas", "Sientes"])

q13 = st.radio("13. Prefieres:", ["Planificar", "Improvisar"])
q14 = st.radio("14. Estilo de vida:", ["Organizado", "Flexible"])
q15 = st.radio("15. Trabajas mejor:", ["Con estructura", "Sin estructura"])
q16 = st.radio("16. Prefieres terminar:", ["Antes", "Último momento"])

# -------------------------------------------------
# ENEAGRAMA
# -------------------------------------------------

st.subheader("Eneagrama")

e1 = st.radio("¿Con cuál te identificas más?", [
    "Perfeccionista",
    "Ayudador",
    "Exitoso",
    "Creativo",
    "Investigador",
    "Leal",
    "Entusiasta",
    "Líder",
    "Pacificador"
])

eneagrama_map = {
    "Perfeccionista":"1w9",
    "Ayudador":"2w3",
    "Exitoso":"3w2",
    "Creativo":"4w5",
    "Investigador":"5w4",
    "Leal":"6w5",
    "Entusiasta":"7w6",
    "Líder":"8w7",
    "Pacificador":"9w1"
}

# -------------------------------------------------
# RESULTADO
# -------------------------------------------------

if st.button("Ver resultado"):

    I = E = N = S = T = F = J = P = 0

    # E / I
    if q1 == "Solo": I += 1
    else: E += 1
    if q2 == "Soledad": I += 1
    else: E += 1
    if q3 == "Observador": I += 1
    else: E += 1
    if q4 == "Individual": I += 1
    else: E += 1

    # S / N
    if q5 == "Hechos": S += 1
    else: N += 1
    if q6 == "Presente": S += 1
    else: N += 1
    if q7 == "Experiencia": S += 1
    else: N += 1
    if q8 == "Ejemplos": S += 1
    else: N += 1

    # T / F
    if q9 == "Lógica": T += 1
    else: F += 1
    if q10 == "Justicia": T += 1
    else: F += 1
    if q11 == "Objetivo": T += 1
    else: F += 1
    if q12 == "Analizas": T += 1
    else: F += 1

    # J / P
    if q13 == "Planificar": J += 1
    else: P += 1
    if q14 == "Organizado": J += 1
    else: P += 1
    if q15 == "Con estructura": J += 1
    else: P += 1
    if q16 == "Antes": J += 1
    else: P += 1

    # MBTI final
    mbti = ""
    mbti += "I" if I >= E else "E"
    mbti += "N" if N >= S else "S"
    mbti += "T" if T >= F else "F"
    mbti += "J" if J >= P else "P"

    eneagrama = eneagrama_map[e1]

    st.success(f"Tu tipo es: {mbti} | Eneagrama: {eneagrama}")

    # -------------------------------------------------
    # COMPATIBILIDAD
    # -------------------------------------------------

    usuario_vec = mbti_to_vec.get(mbti, [0,0,0,0])

    df["vector"] = df["mbti"].apply(lambda x: mbti_to_vec.get(x, [0,0,0,0]))

    df["compatibilidad"] = df["vector"].apply(
        lambda v: cosine_similarity(usuario_vec, v)
    ) * 100

    # -------------------------------------------------
    # RESULTADOS
    # -------------------------------------------------

    st.subheader("Top celebridades compatibles")

    top = df.sort_values("compatibilidad", ascending=False).head(5)

    for _, row in top.iterrows():

        st.markdown(f"### {row['nombre']}")
        st.write(f"MBTI: {row['mbti']} | Eneagrama: {row['eneagrama']}")
        st.write(f"{row['compatibilidad']:.1f}% compatibilidad")

        st.image(row["imagen"], width=150)

        st.markdown("---")

    st.info("Modelo combinado MBTI + Eneagrama (5w4, 3w2, etc.)")
