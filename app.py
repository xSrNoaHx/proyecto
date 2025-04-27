import streamlit as st

st.set_page_config(page_title="Autoevaluación de Burnout", page_icon="🧹", layout="centered")

st.title("Autoevaluación de Burnout para Enfermería 🧹")
st.write("Hola, soy tu asistente virtual de bienestar emocional para enfermería. \n\nHoy realizaremos una autoevaluación interactiva para identificar posibles signos de burnout laboral. \n\n✨ **¡Tu salud mental importa tanto como tu vocación!**")

if 'responses' not in st.session_state:
    st.session_state.responses = []

start = st.radio("\u00bfDeseas iniciar tu autoevaluación?", ("Selecciona una opción", "Sí, iniciar.", "No, salir."))

if start == "Sí, iniciar.":

    # Pregunta 1
    q1 = st.radio("1. ¿Cuántas horas trabajas en promedio cada semana?", ["Menos de 40 horas.", "Entre 40 y 60 horas.", "Más de 60 horas."])
    
    if q1 == "Menos de 40 horas.":
        st.success("\u2728 ¡Bien! Un horario moderado protege tu energía y reduce el riesgo de fatiga crónica.")
        st.session_state.responses.append('bajo')
    elif q1 == "Entre 40 y 60 horas.":
        st.warning("🚫 Cuidado: este rango ya puede incrementar el cansancio acumulativo.")
        st.session_state.responses.append('medio')
    else:
        st.error("🛑 Alerta: una sobrecarga horaria extrema deteriora la calidad de servicio.")
        st.session_state.responses.append('alto')

    # Pregunta 2
    q2 = st.radio("2. ¿Cómo te sientes físicamente al terminar tus turnos?", ["Energizado(a) y satisfecho(a).", "Cansado(a), pero funcional.", "Totalmente agotado(a) física y mentalmente."])

    if q2 == "Energizado(a) y satisfecho(a).":
        st.success("💚 Excelente equilibrio entre exigencia laboral y autocuidado.")
        st.session_state.responses.append('bajo')
    elif q2 == "Cansado(a), pero funcional.":
        st.warning("🔊 Cansancio moderado, observa si se vuelve persistente.")
        st.session_state.responses.append('medio')
    else:
        st.error("🧬 El agotamiento extremo favorece deterioro emocional y físico.")
        st.session_state.responses.append('alto')

    # Pregunta 3
    q3 = st.radio("3. ¿Qué emociones predominan en ti mientras trabajas?", ["Motivación y sentido de propósito.", "Estrés y frustración esporádica.", "Irritación, despersonalización y apatía."])

    if q3 == "Motivación y sentido de propósito.":
        st.success("🌟 Tu propósito es un escudo contra el burnout.")
        st.session_state.responses.append('bajo')
    elif q3 == "Estrés y frustración esporádica.":
        st.warning("🚫 Estrés ocasional aceptable, pero requiere manejo.")
        st.session_state.responses.append('medio')
    else:
        st.error("🫀 Síntomas de burnout avanzado, atención necesaria.")
        st.session_state.responses.append('alto')

    # Pregunta 4
    q4 = st.radio("4. ¿Has presentado síntomas físicos como insomnio, dolores, palpitaciones o problemas digestivos?", ["No, nunca.", "A veces.", "Frecuentemente."])

    if q4 == "No, nunca.":
        st.success("💪 Señal de buen manejo del estrés.")
        st.session_state.responses.append('bajo')
    elif q4 == "A veces.":
        st.warning("⚠️ Atención: podría ser el inicio de sobrecarga.")
        st.session_state.responses.append('medio')
    else:
        st.error("🛑 Alta frecuencia de síntomas de estrés crónico.")
        st.session_state.responses.append('alto')

    # Pregunta 5
    q5 = st.radio("5. ¿Últimamente has sentido que tu trabajo carece de sentido o importancia?", ["Nunca.", "A veces.", "Sí, frecuentemente."])

    if q5 == "Nunca.":
        st.success("🚀 Tu motivación es una gran fortaleza.")
        st.session_state.responses.append('bajo')
    elif q5 == "A veces.":
        st.warning("🚫 Alerta temprana de desgaste emocional.")
        st.session_state.responses.append('medio')
    else:
        st.error("📢 Pérdida de sentido: síntoma principal de burnout.")
        st.session_state.responses.append('alto')

    # Pregunta 6
    q6 = st.radio("6. ¿Has considerado dejar tu trabajo debido al cansancio o estrés?", ["No.", "Sí, ocasionalmente.", "Sí, frecuentemente."])

    if q6 == "No.":
        st.success("💪 Buena resiliencia laboral.")
        st.session_state.responses.append('bajo')
    elif q6 == "Sí, ocasionalmente.":
        st.warning("🔊 Normal, pero vigila su frecuencia.")
        st.session_state.responses.append('medio')
    else:
        st.error("🛑 Alta probabilidad de burnout grave.")
        st.session_state.responses.append('alto')

    # Diagnóstico Final
    if st.button("Obtener resultado final"):
        bajo = st.session_state.responses.count('bajo')
        medio = st.session_state.responses.count('medio')
        alto = st.session_state.responses.count('alto')

        st.subheader("Resultado de tu evaluación 🔍")

        if alto >= 3:
            st.error("Presentas signos claros de burnout. Es urgente atender tu bienestar: busca apoyo psicológico, reajusta tus turnos laborales y trabaja en estrategias de recuperación emocional.")
        elif medio >= 3:
            st.warning("Presentas señales iniciales de fatiga emocional. Es un buen momento para reforzar hábitos de descanso y pedir apoyo institucional si es necesario.")
        else:
            st.success("Tu riesgo de burnout es bajo. ¡Sigue manteniendo tus estrategias de autocuidado y balance laboral!")

        st.info("Recuerda que tu salud emocional es esencial para ofrecer una atención de calidad. \n\n✨ ¡Cuidarte a ti mismo(a) es también cuidar a tus pacientes!")

elif start == "No, salir.":
    st.warning("Gracias por visitarnos. ¡Hasta pronto!")
