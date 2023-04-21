import openai, config, typer
from rich import print
from rich.table import Table

# Def function of Typer execute
def main():
    openai.api_key = config.api_key
    # Title in the console
    print("[bold green]ChatGPT API in Python[/bold green]")

    # Table of the commands
    table = Table("Comando", "Descripción")
    table.add_row("stop", "Salir de la aplicación")
    table.add_row("new", "Nueva conversación")
    # Print of table
    print(table)

    # Contexto del asistente
    context = {"role": "system",
               "content": "Eres un asistente muy útil."}
    messages = [context]

    while True:

        content = __prompt()

        # Exit of iterations.
        if content == "new":
            print("🆕 Nueva conversación creada")
            messages = [context]
            content = __prompt()

        # Add promto of array messages with roll user
        messages.append({"role": "user", "content": content})

        # Execute code, send of messages in apy
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        # Save of responde in variable
        response_content = response.choices[0].message.content
        # Add responde with context of assistant, this is very functional
        messages.append({"role": "assistant", "content": response_content})
        # Response make of user view all responses by IA, more tokens use.
        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")
        # print(f'[green]> [/green][green]{response_content} Tokens Used {response.usage.total_tokens}[/green]')

# Def function private of prompt of menu in the App, 
def __prompt() -> str:
    # Input by User insert a prompts
    prompt = typer.prompt("En que puedo ayudarte")

    # Exit of iterations.
    if prompt == "stop":
        stop = typer.confirm("👀 ¿Estás Seguro?")
        # yes or not response
        if stop:
            raise typer.Abort()
        # If response is not or false, reexecute of function prompt
        return __prompt()            
    
    return prompt

# User TYPER by experience very easy.
if __name__ == "__main__":
    typer.run(main)
