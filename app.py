import streamlit as st

# -------------------------------------------------
# CONFIGURACIÓN
# -------------------------------------------------

st.set_page_config(
    page_title="Personality Compatibility Finder",
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

html, body, [class*="css"] {
    color: #222222;
}

h1, h2, h3, h4, h5, h6, p, label, div {
    color: #222222 !important;
}

.result-box {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #dcdcdc;
    margin-top: 20px;
    color: #222222;
}

section[data-testid="stSidebar"] {
    background-color: #eeeeee;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# TÍTULO
# -------------------------------------------------

st.title("Personality Compatibility Finder")

st.write(
    "Answer the following questions to discover your personality profile "
    "and compatible celebrities."
)

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

st.subheader("Personality Questions")

# 1
q1 = st.radio(
    "1. What sounds more enjoyable?",
    [
        "Analyzing ideas quietly",
        "Going out and trying exciting experiences"
    ]
)

# 2
q2 = st.radio(
    "2. People describe you as:",
    [
        "Reserved and thoughtful",
        "Energetic and expressive"
    ]
)

# 3
q3 = st.radio(
    "3. When making decisions you rely more on:",
    [
        "Logic and objectivity",
        "Emotions and empathy"
    ]
)

# 4
q4 = st.radio(
    "4. Your ideal lifestyle is:",
    [
        "Organized and planned",
        "Flexible and spontaneous"
    ]
)

# 5
q5 = st.radio(
    "5. What motivates you most?",
    [
        "Understanding and knowledge",
        "Helping and connecting with others"
    ]
)

# 6
q6 = st.radio(
    "6. Which describes you better?",
    [
        "Creative and emotional",
        "Confident and dominant"
    ]
)

# 7
q7 = st.radio(
    "7. In social situations you usually:",
    [
        "Observe before participating",
        "Interact immediately"
    ]
)

# 8
q8 = st.radio(
    "8. What is more important to you?",
    [
        "Stability and peace",
        "Adventure and fun"
    ]
)

# 9
q9 = st.radio(
    "9. You prefer:",
    [
        "Abstract ideas and possibilities",
        "Facts and practical information"
    ]
)

# 10
q10 = st.radio(
    "10. During conflict you tend to:",
    [
        "Stay calm and avoid tension",
        "Take control of the situation"
    ]
)

# -------------------------------------------------
# BOTÓN
# -------------------------------------------------

if st.button("Generate Result"):

    # -------------------------------------------------
    # LÓGICA MBTI + ENNEAGRAM
    # -------------------------------------------------

    # 1
    if q1 == "Analyzing ideas quietly":
        I += 1
        tipo5 += 1
    else:
        E += 1
        tipo7 += 1

    # 2
    if q2 == "Reserved and thoughtful":
        I += 1
        tipo5 += 1
    else:
        E += 1
        tipo7 += 1

    # 3
    if q3 == "Logic and objectivity":
        T += 1
        tipo5 += 1
    else:
        F += 1
        tipo2 += 1

    # 4
    if q4 == "Organized and planned":
        J += 1
        tipo9 += 1
    else:
        P += 1
        tipo7 += 1

    # 5
    if q5 == "Understanding and knowledge":
        N += 1
        tipo5 += 1
    else:
        F += 1
        tipo2 += 1

    # 6
    if q6 == "Creative and emotional":
        F += 1
        tipo4 += 1
    else:
        T += 1
        tipo8 += 1

    # 7
    if q7 == "Observe before participating":
        I += 1
        tipo9 += 1
    else:
        E += 1
        tipo7 += 1

    # 8
    if q8 == "Stability and peace":
        J += 1
        tipo9 += 1
    else:
        P += 1
        tipo7 += 1

    # 9
    if q9 == "Abstract ideas and possibilities":
        N += 1
        tipo4 += 1
    else:
        S += 1
        tipo2 += 1

    # 10
    if q10 == "Stay calm and avoid tension":
        F += 1
        tipo9 += 1
    else:
        T += 1
        tipo8 += 1

    # -------------------------------------------------
    # RESULTADO MBTI
    # -------------------------------------------------

    resultado_mbti = ""

    resultado_mbti += "I" if I >= E else "E"
    resultado_mbti += "N" if N >= S else "S"
    resultado_mbti += "T" if T >= F else "F"
    resultado_mbti += "J" if J >= P else "P"

    # -------------------------------------------------
    # RESULTADO ENNEAGRAM
    # -------------------------------------------------

    enneagram_scores = {
        "2w3": tipo2,
        "4w5": tipo4,
        "5w6": tipo5,
        "7w6": tipo7,
        "8w7": tipo8,
        "9w1": tipo9
    }

    resultado_enneagram = max(
        enneagram_scores,
        key=enneagram_scores.get
    )

    # -------------------------------------------------
    # DESCRIPCIONES
    # -------------------------------------------------

    descripciones = {
        "INTJ": "Strategic, analytical and independent.",
        "INTP": "Logical, curious and highly analytical.",
        "ENTJ": "Natural leaders, ambitious and decisive.",
        "ENTP": "Innovative, curious and energetic.",

        "INFJ": "Empathetic, visionary and thoughtful.",
        "INFP": "Creative, emotional and idealistic.",
        "ENFJ": "Charismatic, supportive and inspiring.",
        "ENFP": "Enthusiastic and highly social.",

        "ISTJ": "Responsible, practical and organized.",
        "ISFJ": "Loyal, caring and detail-oriented.",
        "ESTJ": "Efficient, direct and structured.",
        "ESFJ": "Friendly, cooperative and sociable.",

        "ISTP": "Independent, observant and adaptable.",
        "ISFP": "Sensitive, artistic and calm.",
        "ESTP": "Energetic, bold and action-oriented.",
        "ESFP": "Expressive, spontaneous and outgoing."
    }

    # -------------------------------------------------
    # CELEBRIDADES
    # -------------------------------------------------

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

    # -------------------------------------------------
    # RESULTADOS
    # -------------------------------------------------

    st.markdown(
        f'''
        <div class="result-box">
            <h2>Results</h2>
            <p><strong>MBTI:</strong> {resultado_mbti}</p>
            <p><strong>Enneagram:</strong> {resultado_enneagram}</p>
        </div>
        ''',
        unsafe_allow_html=True
    )

    # -------------------------------------------------
    # DESCRIPCIÓN
    # -------------------------------------------------

    st.subheader("Personality Description")

    st.write(descripciones[resultado_mbti])

    # -------------------------------------------------
    # CELEBRIDADES
    # -------------------------------------------------

    st.subheader("Compatible Celebrities")

    for persona in celebridades[resultado_mbti]:
        st.write(f"- {persona}")

    st.markdown("---")

    st.caption(
        "This project uses rule-based personality classification "
        "combined with personality matching concepts."
    )
