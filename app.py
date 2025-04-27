import streamlit as st

st.set_page_config(page_title="Autoevaluación de Burnout", page_icon="🧹", layout="centered")

st.title("Autoevaluación de Burnout para Enfermería 🧹")

if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.history = []
    st.session_state.responses = []

def bot_message(message):
    st.chat_message("assistant").markdown(message)

def user_message(message):
    st.chat_message("user").markdown(message)

questions = [
    {
        "question": "¿Cuántas horas trabajas en promedio cada semana?",
        "options": ["Menos de 40 horas.", "Entre 40 y 60 horas.", "Más de 60 horas."],
        "responses": ["bajo", "medio", "alto"],
        "feedback": [
            "✨ ¡Bien! Un horario moderado protege tu energía y reduce el riesgo de fatiga crónica.",
            "🚫 Cuidado: este rango ya puede incrementar el cansancio acumulativo.",
            "🛑 Alerta: una sobrecarga horaria extrema deteriora la calidad de servicio."
        ]
    },
    {
        "question": "¿Cómo te sientes físicamente al terminar tus turnos?",
        "options": ["Energizado(a) y satisfecho(a).", "Cansado(a), pero funcional.", "Totalmente agotado(a) física y mentalmente."],
        "responses": ["bajo", "medio", "alto"],
        "feedback": [
            "💚 Excelente equilibrio entre exigencia laboral y autocuidado.",
            "🔊 Cansancio moderado, observa si se vuelve persistente.",
            "🧬 El agotamiento extremo favorece deterioro emocional y físico."
        ]
    },
    {
        "question": "¿Qué emociones predominan en ti mientras trabajas?",
        "options": ["Motivación y sentido de propósito.", "Estrés y frustración esporádica.", "Irritación, despersonalización y apatía."],
        "responses": ["bajo", "medio", "alto"],
        "feedback": [
            "🌟 Tu propósito es un escudo contra el burnout.",
            "🚫 Estrés ocasional aceptable, pero requiere manejo.",
            "🫀 Síntomas de burnout avanzado, atención necesaria."
        ]
    },
    {
        "question": "¿Has presentado síntomas físicos como insomnio, dolores, palpitaciones o problemas digestivos?",
        "options": ["No, nunca.", "A veces.", "Frecuentemente."],
        "responses": ["bajo", "medio", "alto"],
        "feedback": [
            "💪 Señal de buen manejo del estrés.",
            "⚠️ Atención: podría ser el inicio de sobrecarga.",
            "🛑 Alta frecuencia de síntomas de estrés crónico."
        ]
    },
    {
        "question": "¿Últimamente has sentido que tu trabajo carece de sentido o importancia?",
        "options": ["Nunca.", "A veces.", "Sí, frecuentemente."],
        "responses": ["bajo", "medio", "alto"],
        "feedback": [
            "🚀 Tu motivación es una gran fortaleza.",
            "🚫 Alerta temprana de desgaste emocional.",
            "📢 Pérdida de sentido: síntoma principal de burnout."
        ]
    },
    {
        "question": "¿Has considerado dejar tu trabajo debido al cansancio o estrés?",
        "options": ["No.", "Sí, ocasionalmente.", "Sí, frecuentemente."],
        "responses": ["bajo", "medio", "alto"],
        "feedback": [
            "💪 Buena resiliencia laboral.",
            "🔊 Normal, pero vigila su frecuencia.",
            "🛑 Alta probabilidad de burnout grave."
        ]
    }
]

# Mostrar historial
for entry in st.session_state.history:
    with st.chat_message(entry['role']):
        st.markdown(entry['content'])

# Flujo del chatbot
if st.session_state.step == 0:
    bot_message("Hola, soy tu asistente virtual de bienestar emocional para enfermería. \n\n✨ Hoy realizaremos una autoevaluación para identificar signos de burnout.\n\n¿Deseas iniciar?")
    if st.button("🌟 Sí, iniciar"):
        st.session_state.history.append({"role": "assistant", "content": "Hola, soy tu asistente virtual de bienestar emocional para enfermería. \n\n✨ Hoy realizaremos una autoevaluación para identificar signos de burnout.\n\n¿Deseas iniciar?"})
        st.session_state.history.append({"role": "user", "content": "Sí, iniciar"})
        st.session_state.step += 1
    if st.button("🚫 No, salir"):
        st.session_state.history.append({"role": "assistant", "content": "Hola, soy tu asistente virtual de bienestar emocional para enfermería. \n\n✨ Hoy realizaremos una autoevaluación para identificar signos de burnout.\n\n¿Deseas iniciar?"})
        st.session_state.history.append({"role": "user", "content": "No, salir"})
        bot_message("Gracias por visitarnos. ¡Hasta pronto!")
else:
    index = st.session_state.step - 1
    if index < len(questions):
        q = questions[index]
        bot_message(q["question"])
        choice = st.radio("", q["options"], key=f"question_{index}")
        if st.button("Enviar", key=f"send_{index}"):
            user_message(choice)
            selected_idx = q["options"].index(choice)
            feedback = q["feedback"][selected_idx]
            bot_message(feedback)
            st.session_state.responses.append(q["responses"][selected_idx])
            st.session_state.history.append({"role": "assistant", "content": q["question"]})
            st.session_state.history.append({"role": "user", "content": choice})
            st.session_state.history.append({"role": "assistant", "content": feedback})
            st.session_state.step += 1
            st.experimental_rerun()
    else:
        # Diagnóstico final
        bajo = st.session_state.responses.count('bajo')
        medio = st.session_state.responses.count('medio')
        alto = st.session_state.responses.count('alto')

        bot_message("🔍 Resultado de tu evaluación:")
        if alto >= 3:
            bot_message("🛑 Presentas signos claros de burnout. Es urgente atender tu bienestar: busca apoyo psicológico y reajusta turnos laborales.")
        elif medio >= 3:
            bot_message("🚫 Presentas señales iniciales de fatiga emocional. Refuerza hábitos de descanso y pide apoyo institucional si es necesario.")
        else:
            bot_message("🌟 Tu riesgo de burnout es bajo. ¡Sigue cuidándote y manteniendo tu equilibrio laboral!")

        bot_message("Recuerda que tu salud emocional es esencial para ofrecer una atención de calidad. \n\n✨ ¡Cuidarte también es cuidar a tus pacientes!")
