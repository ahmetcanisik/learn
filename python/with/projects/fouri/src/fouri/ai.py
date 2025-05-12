from google import genai
from os import getenv

"""
Send ai your prompts and return ai response.
We use 'Gemini 2.0 Flash' ai model.

note: Make sure that your .env file contains GEMINI_API_KEY
ex: ai(prompt="Explain how to use ai")
"""


def send_prompt(prompt: str | None = None):
    if prompt is not None:
        api_key = getenv("GEMINI_API_KEY")
        if api_key is not None:
            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt,
            )

            return response.text
    else:
        raise TypeError(f"Expected type is a string but text is {type(prompt)}")
