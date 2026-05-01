import streamlit as st

st.set_page_config(page_title="MBTI Test", page_icon="🧠", layout="centered")

# 🎨 Título
st.markdown(
    "<h1 style='text-align: center; color: #6C63FF;'>🧠 Test de Personalidad MBTI</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Descubre tu personalidad y conoce celebridades similares ✨</p>",
    unsafe_allow_html=True
)

# 👑 Celebridades
celebridades = {
    "INTJ": ["Elon Musk", "Mark Zuckerberg", "Isaac Newton"],
    "ENTP": ["Tom Hanks", "Robert Downey Jr.", "Sacha Baron Cohen"],
    "INFP": ["Johnny Depp", "Tim Burton", "J.K. Rowling"],
    "ENFP": ["Will Smith", "Robin Williams", "Ellen DeGeneres"],
    "INFJ": ["Martin Luther King Jr.", "Lady Gaga", "Nelson Mandela"],
    "ENFJ": ["Oprah Winfrey", "Barack Obama", "Jennifer Lawrence"],
    "ISTJ": ["Jeff Bezos", "Natalie Portman", "George Washington"],
    "ESTJ": ["Emma Watson", "Hillary Clinton", "Judge Judy"],
    "ISFJ": ["Beyoncé", "Kate Middleton", "Mother Teresa"],
    "ESFJ": ["Taylor Swift", "Bill Clinton", "Steve Harvey"],
    "ISTP": ["Bruce Lee", "Michael Jordan", "Clint Eastwood"],
    "ESTP": ["Ernest Hemingway", "Madonna", "Donald Trump"],
    "ISFP": ["Michael Jackson", "Frida Kahlo", "Prince"],
    "ESFP": ["Marilyn Monroe", "Adele", "Jamie Foxx"],
    "INTP": ["Albert Einstein", "Bill Gates", "Marie Curie"],
    "ENTJ": ["Steve Jobs", "Gordon Ramsay", "Margaret Thatcher"]
}

# 🧠 Descripciones psicográficas
descripciones = {
    "INTJ": "Personas estratégicas, independientes y muy analíticas. Les gusta planear a largo plazo.",
    "ENTP": "Creativos, curiosos y debatidores naturales. Aman explorar ideas nuevas.",
    "INFP": "Idealistas, sensibles y guiados por valores personales profundos.",
    "ENFP": "Entusiastas, sociales y llenos de energía creativa.",
    "INFJ": "Empáticos, intuitivos y con fuerte visión del futuro.",
    "ENFJ": "Líderes naturales, empáticos y orientados a ayudar a otros.",
    "ISTJ": "Responsables, organizados y muy confiables.",
    "ESTJ": "Prácticos, directos y excelentes organizadores.",
    "ISFJ": "Protectores, leales y detallistas.",
    "ESFJ": "Amables, sociales y enfocados en la armonía.",
    "ISTP": "Prácticos, observadores y resolutivos.",
    "ESTP": "Energéticos, espontáneos y orientados a la acción.",
    "ISFP": "Artísticos, sensibles y tranquilos.",
    "ESFP": "Extrovertidos, divertidos y expresivos.",
    "INTP": "Analíticos, lógicos y amantes del conocimiento.",
    "ENTJ": "Líderes natos, estratégicos y decididos."
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

# 🎯 Botón resultado
if st.button("✨ Ver resultado"):

    # reset
    I = E = N = S = T = F = J = P = 0

    # I vs E
    if q1 == "Solo": I += 1
    else: E += 1

    if q2 == "Cansado": I += 1
    else: E += 1

    if q3 == "Reservado": I += 1
    else: E += 1

    if q4 == "Solo": I += 1
    else: E += 1

    # S vs N
    if q5 == "Hechos concretos": S += 1
    else: N += 1

    if q6 == "El presente": S += 1
    else: N += 1

    if q7 == "Instrucciones claras": S += 1
    else: N += 1

    if q8 == "Experiencia": S += 1
    else: N += 1

    # T vs F
    if q9 == "Lógica": T += 1
    else: F += 1

    if q10 == "Justicia": T += 1
    else: F += 1

    if q11 == "Objetivo": T += 1
    else: F += 1

    if q12 == "Analizas": T += 1
    else: F += 1

    # J vs P
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

    st.success(f"🧠 Tu tipo de personalidad es: **{resultado}**")

    # descripción
    st.markdown("### 🧠 Descripción psicográfica:")
    st.write(descripciones[resultado])

    # celebridades
    st.markdown("### ✨ Celebridades con tu tipo:")
    for persona in celebridades[resultado]:
        st.write(f"- {persona}")

    st.markdown("---")
    st.info("Basado en análisis de datos del modelo MBTI.")

    st.write("Este resultado está basado en el modelo MBTI analizado previamente.")
