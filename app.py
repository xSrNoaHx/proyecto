import streamlit as st

st.set_page_config(page_title="Autoevaluación de Burnout", page_icon="🧹", layout="centered")

st.title("Autoevaluación de Burnout para Enfermería 🧹")

if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.history = []
    st.session_state.responses = []

questions = [
    {
        "question": "¿Cuántas horas trabajas en promedio cada semana?",
        "keywords": {"menos": "bajo", "40": "bajo", "60": "medio", "más": "alto"}
    },
    {
        "question": "¿Cómo te sientes físicamente al terminar tus turnos?",
        "keywords": {"energizado": "bajo", "cansado": "medio", "agotado": "alto"}
    },
    {
        "question": "¿Qué emociones predominan en ti mientras trabajas?",
        "keywords": {"motivación": "bajo", "estrés": "medio", "apatía": "alto", "irritación": "alto"}
    },
    {
        "question": "¿Has presentado síntomas físicos como insomnio, dolores, palpitaciones o problemas digestivos?",
        "keywords": {"nunca": "bajo", "a veces": "medio", "frecuentemente": "alto"}
    },
    {
        "question": "¿Últimamente has sentido que tu trabajo carece de sentido o importancia?",
        "keywords": {"nunca": "bajo", "a veces": "medio", "frecuentemente": "alto"}
    },
    {
        "question": "¿Has considerado dejar tu trabajo debido al cansancio o estrés?",
        "keywords": {"no": "bajo", "ocasionalmente": "medio", "frecuentemente": "alto"}
    }
]

# Mostrar historial
for entry in st.session_state.history:
    with st.chat_message(entry['role']):
        st.markdown(entry['content'])

# Flujo del chatbot
if st.session_state.step == 0:
    with st.chat_message("assistant"):
        st.markdown("Hola, soy tu asistente virtual de bienestar emocional para enfermería. \n\n✨ Hoy realizaremos una autoevaluación para identificar signos de burnout.\n\n¿Deseas iniciar? (Responde 'si' o 'no')")
    user_input = st.chat_input("Escribe aquí...")
    if user_input:
        st.session_state.history.append({"role": "user", "content": user_input})
        if "si" in user_input.lower():
            st.session_state.step += 1
            st.session_state.history.append({"role": "assistant", "content": "💬 Comencemos con la evaluación."})
            st.experimental_rerun()
        else:
            st.session_state.history.append({"role": "assistant", "content": "Gracias por visitarnos. ¡Hasta pronto!"})
else:
    index = st.session_state.step - 1
    if index < len(questions):
        current_q = questions[index]
        with st.chat_message("assistant"):
            st.markdown(current_q["question"])
        user_input = st.chat_input("Responde aquí...")
        if user_input:
            st.session_state.history.append({"role": "user", "content": user_input})
            matched = False
            for keyword, risk in current_q["keywords"].items():
                if keyword.lower() in user_input.lower():
                    st.session_state.responses.append(risk)
                    matched = True
                    break
            if not matched:
                st.session_state.responses.append("medio")  # Respuesta neutra si no reconoce
            st.session_state.step += 1
            st.experimental_rerun()
    else:
        # Diagnóstico final
        bajo = st.session_state.responses.count('bajo')
        medio = st.session_state.responses.count('medio')
        alto = st.session_state.responses.count('alto')

        with st.chat_message("assistant"):
            st.markdown("🔍 Resultado de tu evaluación:")
            if alto >= 3:
                st.markdown("🛑 Presentas signos claros de burnout. Es urgente atender tu bienestar: busca apoyo psicológico y reajusta turnos laborales.")
            elif medio >= 3:
                st.markdown("🚫 Presentas señales iniciales de fatiga emocional. Refuerza hábitos de descanso y pide apoyo institucional si es necesario.")
            else:
                st.markdown("🌟 Tu riesgo de burnout es bajo. ¡Sigue cuidándote y manteniendo tu equilibrio laboral!")

            st.markdown("Recuerda que tu salud emocional es esencial para ofrecer una atención de calidad. \n\n✨ ¡Cuidarte también es cuidar a tus pacientes!")

