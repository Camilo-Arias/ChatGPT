import openai
import config

openai.api_key = config.api_key

# Contexto del asistente
messages = [{
    "role": "system",
    "content": "Eres un asistente muy útil."}]

while True:

    content = input("En que puedo ayudarte: ")

    if content == "stop":
        break

    messages.append({"role": "user", "content": content})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    response_content = response.choices[0].message.content

    messages.append({"role": "assistant", "content": response_content})

    print(f'{response.choices[0].message.content} Tokens Used {response.usage.total_tokens}')
