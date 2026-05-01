import streamlit as st

st.title("🧠 Test de Personalidad MBTI")

st.write("Responde las siguientes preguntas para descubrir tu tipo de personalidad")

# Variables
I = E = N = S = T = F = J = P = 0

# Preguntas
q1 = st.radio("1. ¿Prefieres pasar tiempo?", ["Solo", "Con otras personas"])
q2 = st.radio("2. ¿Confías más en?", ["Hechos y detalles", "Ideas y posibilidades"])
q3 = st.radio("3. ¿Tomas decisiones con?", ["Lógica", "Emociones"])
q4 = st.radio("4. ¿Te organizas de forma?", ["Planificada", "Flexible"])

# Sumar puntos
if q1 == "Solo":
    I += 1
else:
    E += 1

if q2 == "Hechos y detalles":
    S += 1
else:
    N += 1

if q3 == "Lógica":
    T += 1
else:
    F += 1

if q4 == "Planificada":
    J += 1
else:
    P += 1

# Resultado
if st.button("Ver resultado"):
    resultado = ""

    resultado += "I" if I >= E else "E"
    resultado += "N" if N >= S else "S"
    resultado += "T" if T >= F else "F"
    resultado += "J" if J >= P else "P"

    st.success(f"Tu tipo de personalidad es: {resultado}")

    st.write("Este resultado está basado en el modelo MBTI analizado previamente.")