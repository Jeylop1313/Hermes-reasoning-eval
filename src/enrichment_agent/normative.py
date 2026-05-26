NORMATIVE_PROMPT = """
Eres HERMES. Has completado el SEC 1 y el SEC 2.
Ahora ejecuta el SEC 3 — Significancia Normativa: evalúa si el autor 
señala que estándares, valores o normas están en juego.

COMENTARIO: {comment}
CONTEXTO DEL AUTOR: {Avatar}

SALIDA SEC 1: {relevance_output}
SALIDA SEC 2: {implication_output}
SALIDA SEC 3: {coping_output}

---

## SEC 3 — SIGNIFICANCIA NORMATIVA

Responde cada pregunta en 1-2 oraciones.
Cita la palabra o frase específica del comentario que sustenta 
tu respuesta. Si no existe evidencia lingüística, escribe "sin señal."

Estándares Internos: ¿Señala el autor que un valor personal, 
código moral o ideal propio está en juego — ya sea violado o sostenido?
Busca: lenguaje moral, expresiones de principio personal, o 
señales de orgullo o vergüenza.

Estándares Externos: ¿Invoca el autor normas sociales compartidas, 
expectativas grupales o valores colectivos?
Busca: lenguaje colectivo, llamados a la acción dirigidos a un grupo, 
o apelaciones a lo socialmente aceptable.

Posicionamiento: ¿Cómo se posiciona el autor respecto al estándar 
que está invocando?
Distingue tres casos:
- Juez de otros: condena el comportamiento o carácter de otra persona
- Juez de sí mismo: condena su propio comportamiento o expresa 
  frustración ante su propio fracaso en cumplir un estándar — esto 
  señala ira dirigida hacia adentro, no tristeza
- Defensor: aboga por una norma positiva o acción colectiva

Esto separa la indignación moral hacia otros (ira), 
la frustración autodirigida (ira) y la aspiración moral (optimismo).
⚠ El juicio negativo autodirigido no es tristeza — es ira 
sin atribución externa.

## SÍNTESIS
Completa estos tres campos. Sin secciones adicionales, sin elaboración 
más allá de lo que requieren los tres campos. Detente inmediatamente 
después del tercer campo.
"""