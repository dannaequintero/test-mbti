import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Test de Compatibilidad de Personalidad",
    page_icon="🧠",
    layout="centered"
)

st.title("Test de Compatibilidad de Personalidad")

# ---------------- CSV ----------------

df = pd.read_csv("celebridades_mbti.csv")

# ---------------- MBTI VECTOR ----------------

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

# ---------------- DESCRIPCIÓN ----------------

mbti_desc = {
    "INTJ":"Estratega, independiente y analítico.",
    "INTP":"Lógico, curioso y teórico.",
    "ENTJ":"Líder fuerte y orientado a resultados.",
    "ENTP":"Creativo y debatidor.",
    "INFJ":"Empático e intuitivo.",
    "INFP":"Idealista y sensible.",
    "ENFJ":"Carismático y social.",
    "ENFP":"Energético y creativo.",
    "ISTJ":"Responsable y organizado.",
    "ISFJ":"Leal y protector.",
    "ESTJ":"Directo y estructurado.",
    "ESFJ":"Social y cooperativo.",
    "ISTP":"Práctico y observador.",
    "ISFP":"Artístico y sensible.",
    "ESTP":"Energético y espontáneo.",
    "ESFP":"Extrovertido y expresivo."
}

# ---------------- CUESTIONARIO ----------------

st.subheader("Cuestionario")

q1 = st.radio("Prefieres:", ["Solo", "Con gente"])
q2 = st.radio("Te recargas con:", ["Soledad", "Socializar"])
q3 = st.radio("En eventos eres:", ["Observador", "Participativo"])
q4 = st.radio("Prefieres trabajar:", ["Individual", "Equipo"])

q5 = st.radio("Prefieres:", ["Hechos", "Ideas"])
q6 = st.radio("Te enfocas en:", ["Presente", "Futuro"])
q7 = st.radio("Confías en:", ["Experiencia", "Intuición"])
q8 = st.radio("Aprendes mejor con:", ["Ejemplos", "Conceptos"])

q9 = st.radio("Decides con:", ["Lógica", "Emoción"])
q10 = st.radio("Valoras:", ["Justicia", "Empatía"])
q11 = st.radio("Eres más:", ["Objetivo", "Comprensivo"])
q12 = st.radio("En conflictos:", ["Analizas", "Sientes"])

q13 = st.radio("Prefieres:", ["Planificar", "Improvisar"])
q14 = st.radio("Estilo de vida:", ["Organizado", "Flexible"])
q15 = st.radio("Trabajas mejor:", ["Con estructura", "Sin estructura"])
q16 = st.radio("Prefieres terminar:", ["Antes", "Último momento"])

# ---------------- RESULTADO ----------------

if st.button("Ver resultado"):

    I = E = N = S = T = F = J = P = 0

    if q1 == "Solo": I += 1
    else: E += 1
    if q2 == "Soledad": I += 1
    else: E += 1
    if q3 == "Observador": I += 1
    else: E += 1
    if q4 == "Individual": I += 1
    else: E += 1

    if q5 == "Hechos": S += 1
    else: N += 1
    if q6 == "Presente": S += 1
    else: N += 1
    if q7 == "Experiencia": S += 1
    else: N += 1
    if q8 == "Ejemplos": S += 1
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

    mbti = ""
    mbti += "I" if I >= E else "E"
    mbti += "N" if N >= S else "S"
    mbti += "T" if T >= F else "F"
    mbti += "J" if J >= P else "P"

    st.success(f"Tu MBTI es: {mbti}")

    # ---------------- PERSONALIDAD ----------------

    st.subheader("Tu personalidad")

    st.info(mbti_desc[mbti])

    # ---------------- ENEAGRAMA ----------------

    if mbti in ["INTJ","INTP"]:
        eneagrama = "5w4"
    elif mbti in ["ENTJ","ESTJ"]:
        eneagrama = "8w7"
    elif mbti in ["ENFP","ESFP"]:
        eneagrama = "7w6"
    elif mbti in ["INFJ","INFP"]:
        eneagrama = "4w5"
    elif mbti in ["ENFJ","ESFJ"]:
        eneagrama = "2w3"
    else:
        eneagrama = "6w5"

    st.write(f"Eneagrama: {eneagrama}")

    # ---------------- VECTOR USUARIO ----------------

    user_vector = np.array([
        T > F,
        E > I,
        N > S,
        J > P,
        F > T,
        I > E,
        T > F,
        J > P
    ]).astype(int)

    df["vector"] = df.apply(lambda row: np.array([
        row["analitico"],
        row["social"],
        row["creativo"],
        row["lider"],
        row["emocional"],
        row["introversion"],
        row["logica"],
        row["estructura"]
    ]), axis=1)

    df["compatibilidad"] = df["vector"].apply(
        lambda v: cosine_similarity(user_vector, v)
    ) * 100

    # ---------------- RESULTADOS ----------------

    st.subheader("Top compatibilidad")

    top = df.sort_values("compatibilidad", ascending=False).head(5)

    for _, row in top.iterrows():

        st.markdown("---")

        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(row["imagen"], use_container_width=True)

        with col2:
            st.markdown(f"### {row['nombre']}")
            st.write(f"MBTI: {row['mbti']} | Eneagrama: {row['eneagrama']}")
            st.metric("Compatibilidad", f"{row['compatibilidad']:.1f}%")

            # explicación del match
            st.caption(
                "Coincidencia basada en estructura de personalidad (MBTI + rasgos de comportamiento)"
            )

    st.markdown("---")
    st.success("Modelo híbrido: MBTI + Eneagrama + análisis vectorial de personalidad")
