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

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# -------------------------------------------------
# PREGUNTAS
# -------------------------------------------------

q1 = st.radio("Prefieres:", ["Solo", "Con gente"])
q2 = st.radio("Decides con:", ["Lógica", "Emoción"])
q3 = st.radio("Estilo:", ["Planificado", "Espontáneo"])
q4 = st.radio("Prefieres:", ["Ideas", "Hechos"])

# -------------------------------------------------
# RESULTADO
# -------------------------------------------------

if st.button("Ver resultado"):

    I = 1 if q1 == "Solo" else 0
    E = 1 if q1 == "Con gente" else 0

    T = 1 if q2 == "Lógica" else 0
    F = 1 if q2 == "Emoción" else 0

    J = 1 if q3 == "Planificado" else 0
    P = 1 if q3 == "Espontáneo" else 0

    N = 1 if q4 == "Ideas" else 0
    S = 1 if q4 == "Hechos" else 0

    resultado = ""
    resultado += "I" if I >= E else "E"
    resultado += "N" if N >= S else "S"
    resultado += "T" if T >= F else "F"
    resultado += "J" if J >= P else "P"

    st.success(f"Tu tipo MBTI es: {resultado}")

    usuario_vec = mbti_to_vec.get(resultado, [0,0,0,0])

    df["vector"] = df["mbti"].apply(lambda x: mbti_to_vec.get(x, [0,0,0,0]))

    df["compatibilidad"] = df["vector"].apply(
        lambda v: cosine_similarity(usuario_vec, v)
    ) * 100

    top = df.sort_values("compatibilidad", ascending=False).head(5)

    st.subheader("Top celebridades compatibles")

    for _, row in top.iterrows():

        st.markdown(f"### {row['nombre']}")
        st.write(f"{row['compatibilidad']:.1f}% compatibilidad")

        # IMAGEN AUTOMÁTICA (sin CSV)
        st.image(
            f"https://source.unsplash.com/300x300/?{row['nombre']}",
            width=150
        )

        st.markdown("---")
