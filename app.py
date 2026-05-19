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
st.write("Responde las preguntas y descubre tu tipo MBTI y compatibilidad.")

# -------------------------------------------------
# CARGAR CSV (IMPORTANTE)
# -------------------------------------------------

df = pd.read_csv("celebridades_mbti.csv")

# -------------------------------------------------
# MAPEO MBTI → VECTORES
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
# PREGUNTAS
# -------------------------------------------------

st.subheader("Cuestionario")

q1 = st.radio("1. ¿Prefieres estar solo o con gente?", ["Solo", "Con gente"])
q2 = st.radio("2. Decides con:", ["Lógica", "Emoción"])
q3 = st.radio("3. Tu estilo es:", ["Planificado", "Espontáneo"])
q4 = st.radio("4. Prefieres:", ["Ideas", "Hechos"])
q5 = st.radio("5. Eres más:", ["Reservado", "Sociable"])

# -------------------------------------------------
# BOTÓN RESULTADO
# -------------------------------------------------

if st.button("Ver resultado"):

    # ---------------- MBTI ----------------

    I = 1 if q1 == "Solo" else 0
    E = 1 if q1 == "Con gente" else 0

    T = 1 if q2 == "Lógica" else 0
    F = 1 if q2 == "Emoción" else 0

    J = 1 if q3 == "Planificado" else 0
    P = 1 if q3 == "Espontáneo" else 0

    N = 1 if q4 == "Ideas" else 0
    S = 1 if q4 == "Hechos" else 0

    resultado_mbti = ""
    resultado_mbti += "I" if I >= E else "E"
    resultado_mbti += "N" if N >= S else "S"
    resultado_mbti += "T" if T >= F else "F"
    resultado_mbti += "J" if J >= P else "P"

    st.success(f"Tu tipo MBTI es: {resultado_mbti}")

    # ---------------- VECTOR USUARIO ----------------

    usuario_vec = mbti_to_vec.get(resultado_mbti, [0,0,0,0])

    # ---------------- VECTOR DATASET ----------------

    df["vector"] = df["mbti"].apply(
        lambda x: mbti_to_vec.get(x, [0,0,0,0])
    )

    # ---------------- SIMILITUD ----------------

    df["compatibilidad"] = df["vector"].apply(
        lambda v: cosine_similarity(usuario_vec, v)
    )

    df["compatibilidad"] = df["compatibilidad"] * 100

    # ---------------- RESULTADOS TOP ----------------

    st.subheader("Top celebridades compatibles")

    top = df.sort_values("compatibilidad", ascending=False).head(5)

    for _, row in top.iterrows():
        st.write(f"⭐ {row['nombre']} - {row['compatibilidad']:.1f}%")

    # ---------------- EXTRA INFO ----------------

    st.markdown("---")
    st.info("Sistema basado en similitud vectorial de personalidad MBTI.")
