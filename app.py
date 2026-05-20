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

# ---------------- DESCRIPCIONES MBTI ----------------

mbti_desc = {
    "INTJ":"Personas estratégicas, independientes y muy analíticas.",
    "INTP":"Analíticos, curiosos y amantes de la lógica.",
    "ENTJ":"Líderes naturales y orientados a resultados.",
    "ENTP":"Creativos, ingeniosos y debatidores.",
    "INFJ":"Intuitivos y empáticos con visión profunda.",
    "INFP":"Idealistas guiados por valores.",
    "ENFJ":"Carismáticos y líderes sociales.",
    "ENFP":"Entusiastas y creativos.",
    "ISTJ":"Responsables y organizados.",
    "ISFJ":"Leales y protectores.",
    "ESTJ":"Directos y organizadores.",
    "ESFJ":"Sociales y cooperativos.",
    "ISTP":"Prácticos y observadores.",
    "ISFP":"Artísticos y sensibles.",
    "ESTP":"Energéticos y espontáneos.",
    "ESFP":"Extrovertidos y expresivos."
}

# ---------------- PREGUNTAS ----------------

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

    st.success(f"MBTI: {mbti} | Eneagrama: {eneagrama}")

    # ---------------- DESCRIPCIÓN ----------------

    st.subheader("Tu personalidad")

    st.write(mbti_desc[mbti])

    eneagrama_desc = {
        "5w4":"Observador, introspectivo y creativo.",
        "5w6":"Analítico y lógico.",
        "4w5":"Artístico y emocional.",
        "3w2":"Orientado al éxito.",
        "7w6":"Optimista y energético.",
        "8w7":"Líder fuerte.",
        "2w3":"Empático y social.",
        "6w5":"Leal y cauteloso.",
        "9w1":"Pacífico y equilibrado."
    }

    st.write(eneagrama_desc[eneagrama])

    # ---------------- VECTOR USUARIO (AQUÍ ESTÁ LA MEJORA) ----------------

    user_vector = np.array([
        T > F,   # analítico
        E > I,   # social
        N > S,   # creativo
        J > P,   # líder
        F > T,   # emocional
        I > E,   # introversión
        T > F,   # lógica
        J > P    # estructura
    ]).astype(int)

    # ---------------- VECTOR DATASET ----------------

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

    st.subheader("Top celebridades compatibles")

    top = df.sort_values("compatibilidad", ascending=False).head(5)

    for _, row in top.iterrows():

        st.markdown(f"### {row['nombre']}")
        st.write(f"MBTI: {row['mbti']} | Eneagrama: {row['eneagrama']}")
        st.write(f"Compatibilidad: {row['compatibilidad']:.1f}%")

        st.image(row["imagen"], use_container_width=True)

        st.markdown("---")

    st.info("Modelo híbrido: MBTI + Eneagrama + categorías de personalidad")
