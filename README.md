# Chatbot Helpdesk con RAG

## Descripción
Este proyecto implementa un chatbot de soporte técnico para la empresa Implementos, utilizando modelos de lenguaje (LLM) y técnicas de Retrieval-Augmented Generation (RAG).

El objetivo es mejorar la atención de usuarios mediante respuestas automáticas basadas en una base de conocimientos, y generar tickets en caso de no encontrar solución.

---

## ¿Cómo funciona?

1. El usuario ingresa una consulta.
2. El sistema busca información relevante en la base de conocimientos (RAG).
3. Se envía el contexto al modelo de lenguaje (LLM).
4. El modelo genera una respuesta basada en la información encontrada.
5. Si no hay solución, se genera automáticamente un ticket.

---

## Tecnologías utilizadas

- Python
- OpenAI API
- python-dotenv

---

## Requisitos

- Python 3.x
- Librerías:
  - openai
  - python-dotenv

---

## Instalación

Instalar dependencias con:

```
pip install openai python-dotenv
```

---

## Configuración

Crear un archivo `.env` con las siguientes variables:

```
GITHUB_TOKEN=tu_api_key
OPENAI_BASE_URL=...
```

---

## Ejecución

Ejecutar el archivo:

```
python chatbot.py
```

Luego escribir una consulta en consola.

---

## Funcionalidades

- Respuestas automáticas
- Recuperación de información (RAG)
- Clasificación de prioridad
- Generación de tickets

---

## Ejemplo

**Usuario:** Error 403  
**Respuesta:** Verificar credenciales  

---

## Autor

Estudiantes de DUOCUC - Ingeniería de Soluciones con IA
