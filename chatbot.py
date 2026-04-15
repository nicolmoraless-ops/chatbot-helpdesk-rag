from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("GITHUB_TOKEN")
)

# Base de conocimiento (RAG)
base_conocimiento = [
    "Error 403: ocurre por falta de permisos. Solución: verificar credenciales.",
    "VPN: problemas de conexión suelen ser por credenciales incorrectas.",
    "Servidor caído: escalar inmediatamente a soporte técnico.",
    "Sistema lento: puede deberse a alta carga del servidor.",
    "Error de acceso: verificar usuario y contraseña."
]

# Recuperación de contexto (RAG)
def recuperar_contexto(pregunta):
    pregunta = pregunta.lower()
    resultados = []

    for doc in base_conocimiento:
        if any(p in doc.lower() for p in pregunta.split()):
            resultados.append(doc)

    return "\n".join(resultados[:2])

# Clasificación de prioridad
def clasificar_prioridad(texto):
    texto = texto.lower()

    if "caido" in texto or "no funciona" in texto:
        return "Alta"
    elif "lento" in texto:
        return "Media"
    else:
        return "Baja"

# Generación de tickets
contador_tickets = 1

def generar_ticket():
    global contador_tickets
    ticket = f"TICKET-{contador_tickets:03d}"
    contador_tickets += 1
    return f"No se encontró solución. Se generó el ticket {ticket}"

# Función principal
def obtener_respuesta(pregunta):
    contexto = recuperar_contexto(pregunta)

    if contexto == "":
        return generar_ticket()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.2,
        max_tokens=120,
        messages=[
            {
                "role": "system",
                "content": "Responde solo usando el contexto entregado."
            },
            {
                "role": "user",
                "content": f"Contexto:\n{contexto}\n\nPregunta:\n{pregunta}"
            }
        ]
    )

    respuesta = response.choices[0].message.content
    prioridad = clasificar_prioridad(pregunta)

    return f"{respuesta}\n\nPrioridad: {prioridad}"

# Ejemplo de uso en consola
if __name__ == "__main__":
    while True:
        pregunta = input("Usuario: ")
        if pregunta.lower() == "salir":
            break

        respuesta = obtener_respuesta(pregunta)
        print("Soporte:", respuesta)
