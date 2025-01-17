def get_question_prompt(domain: str) -> str:
    return f"""
Genera una pregunta de examen PMP del dominio '{domain}' con el siguiente formato:
- Una pregunta relacionada con gestión de proyectos específicamente del dominio {domain}
- 4 opciones de respuesta (A, B, C, D)
- Marca claramente cuál es la respuesta correcta
- Proporciona una explicación de por qué esa es la respuesta correcta

El formato de respuesta debe ser exactamente así:

PREGUNTA: [texto de la pregunta]
A) [opción A]
B) [opción B]
C) [opción C]
D) [opción D]
RESPUESTA CORRECTA: [letra de la opción correcta]
EXPLICACIÓN: [explicación de la respuesta]
"""