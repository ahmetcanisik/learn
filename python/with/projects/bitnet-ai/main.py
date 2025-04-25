#!/usr/bin/env python3
from os import system
from rich import print
from pyfiglet import Figlet
from rich.markdown import Markdown
from transformers import AutoModelForCausalLM, AutoTokenizer

DEFAULTOPTIONS = {
    "name": "BitNet AI Interface",
    "input": "talk with ai",
    "history_length": 4
}

class AIInterface:
    def __init__(self, options=DEFAULTOPTIONS):
        self.options = options
        self.history = []  # Store conversation history
        self.logo = Figlet(font='slant')
        
        # The key fix: add trust_remote_code=True
        model_name = "microsoft/bitnet-b1.58-2B-4T"
        print(f"Loading model: {model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
        
        self.update()
        
    def talk(self, prompt: str = None) -> str:
        if prompt is None:
            raise ValueError("prompt is missing!")
        
        # Add user prompt to history
        self.history.append({
            "role": "user",
            "content": prompt
        })
        
        # Prepare context from history if there's any
        context = ""
        if len(self.history) > 1:  # If there's previous conversation
            for item in self.history[:-1]:  # Exclude the current prompt
                prefix = "User: " if item["role"] == "user" else "AI: "
                context += prefix + item["content"] + "\n"
        
        # Combine context with current prompt
        full_prompt = context + "User: " + prompt + "\nAI: "
        
        # Generate response using the model
        inputs = self.tokenizer(full_prompt, return_tensors="pt")
        output = self.model.generate(
            inputs["input_ids"], 
            max_length=len(inputs["input_ids"][0]) + 150,  # Dynamic length based on input + some extra tokens
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            pad_token_id=self.tokenizer.eos_token_id
        )
        
        # Decode the response, extract only the new part
        full_response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        ai_response = full_response[len(full_prompt):]
        
        # Clean up the response - stop at the next "User:" if present
        if "User:" in ai_response:
            ai_response = ai_response.split("User:")[0].strip()
        
        # Add AI response to history
        self.history.append({
            "role": "assistant",
            "content": ai_response
        })
        
        # Trim history if needed
        if len(self.history) > self.options["history_length"] * 2:
            self.history = self.history[-self.options["history_length"]*2:]
            
        return ai_response

    def display_history(self):
        """Display conversation history"""
        for item in self.history:
            role = item["role"]
            content = item["content"]
            if role == "user":
                print(f"[bold blue]You[/bold blue]: {content}")
            else:
                print(f"[bold green]AI[/bold green]: {content}")

    def ask(self):
        print(f"[bold magenta]{self.options['input']}[/bold magenta]", end="")
        prompt = input(": ")
        
        if prompt.lower() in ["exit", "quit", "bye"]:
            print("[bold red]Exiting...[/bold red]")
            return False
        
        # Get AI response
        response = self.talk(prompt)
        
        # Display response
        print(Markdown(f"**AI**: {response}"))
        
        return True
        
    def update(self):
        system("clear")
    
        # Print logo
        print(self.logo.renderText(self.options["name"]), end="\n")
        
        # Display conversation history
        self.display_history()
        
    def run(self):
        """Main conversation loop"""
        while True:
            self.update()
            if not self.ask():
                break
        
def main():
    ai = AIInterface()
    ai.run()

if __name__ == "__main__":
    main()