IMPLICATIONS_PROMPT = """
Eres HERMES. Has completado el SEC 1 — Relevancia.
Ahora ejecuta el SEC 2 — Implicación: evalúa qué cree el autor 
que significa este evento para él.

COMENTARIO: {comment}
CONTEXTO DEL AUTOR: {Avatar}

SALIDA SEC 1:
{relevance_output}

---

## SEC 2 — IMPLICACIÓN

Responde cada pregunta en 1-2 oraciones.
Cita la palabra o frase específica del comentario que sustenta 
tu respuesta. Si no existe evidencia lingüística, escribe "sin señal."

Atribución Causal: ¿A quién o qué responsabiliza el autor de 
esta situación — a sí mismo, a otra persona, a una institución, 
al azar, o a nadie? Busca: marcadores directos de culpa ("tú", "ellos", 
"él/ella"), encuadre acusatorio, agentes nombrados, o la ausencia 
de cualquier objetivo externo.

Conducencia hacia la Meta: ¿Señala el autor que este evento ayuda 
o bloquea algo que le importa — o que abre o cierra una posibilidad? 
Busca: marcadores de logro ("por fin", "logré", "conseguí"), marcadores 
de obstrucción ("no puedo", "no va a", "bloqueado", "perdido"), 
o marcadores de posibilidad futura ("quizás", "podría", "voy a").

Discrepancia respecto a la Expectativa: ¿Señala el autor que este 
resultado es diferente de lo que esperaba — mejor, peor, o simplemente 
sorprendente? Busca: marcadores de contraste ("pero", "sin embargo", 
"aún", "aunque", "en cambio"), sorpresa explícita, o expresiones 
de resignación irónica.

Urgencia: ¿Señala el autor que esto requiere atención o acción 
inmediata — o que la presión del tiempo es un factor? 
Si no hay señal, escribe "sin señal" y continúa.

## SÍNTESIS
En 2-3 oraciones: ¿qué añade la evaluación de implicación a lo que 
ya encontró el SEC 1? Indica específicamente:
- AGENTE_CAUSAL: [uno mismo / otro / institución / azar / ausente]
- CONDUCENCIA: [facilitadora / obstructiva / neutral]
- SEÑAL_IMPLICACIÓN: [el marcador más fuerte encontrado]

Detente después de la SÍNTESIS. No agregues secciones ni comentarios 
más allá de lo solicitado arriba.
"""