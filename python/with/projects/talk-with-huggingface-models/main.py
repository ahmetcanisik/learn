#!/usr/bin/env python3
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
from os import getenv, system
from rich import print
from pyfiglet import Figlet

load_dotenv()

DEFAULTOPTIONS = {
    "name": "AIInterface",
    "input": "talk with ai"
}

class AIInterface:
    def __init__(self, options = DEFAULTOPTIONS):
        self.options = options
        self.history: list[str] = []
        self.logo = Figlet(font='slant')
        self.client = InferenceClient(
            provider="fireworks-ai",
            api_key=getenv("HUGGINGFACE_API_KEY"),
        )
        self.update()      
        
    def talk(self, prompt: str = None) -> str:
    
        if prompt is None:
            raise ValueError("prompt not found!")
        
        print("thinking...")
        completion = self.client.chat.completions.create(
            model="meta-llama/Llama-4-Maverick-17B-128E-Instruct",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ],
            max_tokens=512,
        )
        
        if not completion:
            raise ValueError("Completion not found!")
        
        return completion.choices[0].message.content

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
            if i >= (len(self.history) - 3):
                text = f"[bold red]{message}[/bold red]" if i % 2 == 0 else f"[bold blue]{message}[/bold blue]"
                print(text, end="\n")
                
        self.ask()
         

def main():
    AIInterface()
    
if __name__ == "__main__":
    main()