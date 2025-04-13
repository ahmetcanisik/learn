#!/usr/bin/env python3
from google import genai
from dotenv import load_dotenv
from os import getenv, system
from rich import print
from pyfiglet import Figlet
from rich.markdown import Markdown

load_dotenv()

DEFAULTOPTIONS = {
    "name": "AIInterface",
    "input": "talk with ai",
    "history_length": 4
}

class AIInterface:
    def __init__(self, options = DEFAULTOPTIONS):
        self.options = options
        self.history: list[str] = []
        self.logo = Figlet(font='slant')
        self.client = genai.Client(api_key=getenv("GEMINI_API_KEY"))
        self.update()      
        
    def talk(self, prompt: str = None) -> str:
    
        if prompt is None:
            raise ValueError("prompt not found!")
        
        print("thinking...")
        completion = self.client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        
        if not completion:
            raise ValueError("Completion not found!")
        
        return completion.text

    def ask(self):
        print(f"[bold magenta]{self.options["input"]}[/bold magenta]", end="")
        prompt = input(": ")
        res = self.talk(prompt)
        self.history.append(prompt)
        self.history.append(res)
        self.update()
        
    def update(self):
        system("clear")
    
        # print logo
        print(self.logo.renderText(self.options["name"]), end="\n")
        
        # print three latest message
        for i, message in enumerate(self.history):
            if i >= (len(self.history) - self.options["history_length"]):
                # Check if this is one of the last two messages
                is_recent = i >= (len(self.history) - 2)
                
                if i % 2 == 0:
                    if is_recent:
                        print(f"[bold blue]YOU:[/bold blue] {message}")
                    else:
                        print(f"[dim blue]YOU:[/dim blue] {message}")
                else:
                    if is_recent:
                        print("[bold red]GEMINI:[/bold red]", end=" ")
                        print(Markdown(message))
                    else:
                        print("[dim red]GEMINI:[/dim red]", end=" ")
                        print(Markdown(message))
                
        self.ask()
         

def main():
    AIInterface()
    
    print(f"API Key loaded: {getenv('GEMINI_API_KEY')}")
    
if __name__ == "__main__":
    main()