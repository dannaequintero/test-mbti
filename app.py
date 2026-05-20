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
    "INTJ":"Personas estratégicas, independientes y muy analíticas. Les gusta planear a largo plazo.",
    "INTP":"Analíticos, curiosos y amantes de la lógica y la teoría.",
    "ENTJ":"Líderes naturales, decididos y orientados a resultados.",
    "ENTP":"Creativos, ingeniosos y amantes del debate y nuevas ideas.",
    "INFJ":"Intuitivos, empáticos y con fuerte visión del futuro.",
    "INFP":"Idealistas, sensibles y guiados por sus valores personales.",
    "ENFJ":"Carismáticos, empáticos y líderes sociales naturales.",
    "ENFP":"Entusiastas, creativos y llenos de energía social.",
    "ISTJ":"Responsables, organizados y muy confiables.",
    "ISFJ":"Protectores, leales y detallistas.",
    "ESTJ":"Prácticos, directos y excelentes organizadores.",
    "ESFJ":"Amables, sociales y enfocados en la armonía.",
    "ISTP":"Prácticos, observadores y resolutivos.",
    "ISFP":"Artísticos, sensibles y tranquilos.",
    "ESTP":"Energéticos, espontáneos y orientados a la acción.",
    "ESFP":"Extrovertidos, divertidos y expresivos."
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

    # eneagrama automático
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
        "5w4":"Observador, introspectivo y creativo. Busca entender el mundo en profundidad.",
        "5w6":"Analítico, lógico y orientado a la seguridad y conocimiento.",
        "4w5":"Emocional, artístico y muy introspectivo.",
        "3w2":"Orientado al éxito, sociable y competitivo.",
        "7w6":"Optimista, energético y busca nuevas experiencias.",
        "8w7":"Líder fuerte, dominante y seguro.",
        "2w3":"Empático, sociable y orientado a ayudar.",
        "6w5":"Leal, cauteloso y analítico.",
        "9w1":"Pacífico, equilibrado y evita conflictos."
    }

    st.write(eneagrama_desc[eneagrama])

    # ---------------- COMPATIBILIDAD ----------------

    usuario_vec = mbti_to_vec.get(mbti, [0,0,0,0])
    df["vector"] = df["mbti"].apply(lambda x: mbti_to_vec.get(x, [0,0,0,0]))

    df["compatibilidad"] = df["vector"].apply(
        lambda v: cosine_similarity(usuario_vec, v)
    ) * 100

    st.subheader("Top celebridades compatibles")

    top = df.sort_values("compatibilidad", ascending=False).head(5)

    for _, row in top.iterrows():

        st.markdown(f"### {row['nombre']}")
        st.write(f"MBTI: {row['mbti']} | Eneagrama: {row['eneagrama']}")
        st.write(f"{row['compatibilidad']:.1f}% compatibilidad")

        st.image(row["imagen"], width=150)

        st.markdown("---")

    st.info("Modelo MBTI + Eneagrama con interpretación psicológica")
