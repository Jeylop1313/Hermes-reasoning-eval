COPING_PROMPT = """
Eres HERMES. Has completado el SEC 1, SEC 2 y SEC 3.
Ahora ejecuta el SEC 4 — Potencial de Afrontamiento: evalúa qué señala 
el autor sobre su capacidad para influir o adaptarse a esta situación.

COMENTARIO: {comment}
CONTEXTO DEL AUTOR: {Avatar}

SALIDA SEC 1: {relevance_output}
SALIDA SEC 2: {implication_output}

---

## SEC 3 — POTENCIAL DE AFRONTAMIENTO

Responde cada pregunta en 1-2 oraciones.
Cita la palabra o frase específica del comentario que sustenta 
tu respuesta. Si no existe evidencia lingüística, escribe "sin señal."

Control: ¿Señala el autor si la situación puede ser influenciada 
o cambiada — por alguien? Busca: verbos imperativos dirigidos a otros, 
expresiones de posibilidad o imposibilidad, lenguaje que enmarca 
la situación como solucionable o permanente.

Poder: ¿Señala el autor si personalmente tiene los recursos, 
la autoridad o la capacidad para actuar sobre esta situación? 
Busca: marcadores de agencia en primera persona, expresiones de 
impotencia o empoderamiento, marcadores de posición social o 
acceso a recursos.

Ajuste: Si el autor no puede controlar o cambiar la situación, 
¿señala alguna capacidad para aceptarla, adaptarse o reencuadrarla? 
Busca: lenguaje de resignación, marcadores de reencuadre, expresiones 
de seguir adelante, o aceptación de un resultado inalterable.

## SÍNTESIS
No generes nuevo razonamiento. Observa lo que encontraste arriba:
- ¿Control encontró una señal de que la situación puede cambiarse?
- ¿Poder encontró una señal de que el autor puede actuar sobre ella?
- ¿Ajuste encontró una señal de que el autor puede aceptarla o reencuadrarla?
"""