#!/usr/bin/env python3
import re

def main():
    print(parse_urls(input("Enter your text: ").strip()))


def parse_urls(text: str = None) -> list:
    if text is None:
        raise ValueError("Please specify the text!")
    
    return re.findall(r'(?:https?://)?(?:[\w-]+\.)*[\w-]+\.[\w-]{2,63}', text, re.IGNORECASE)
    
def parse_emails(text: str = None) -> list:
    if text is None:
        raise ValueError("Please specify the text!")
    
    return re.findall(r'[\w._%+-]+@[\w.-]+\.[\w]{2,63}', text, re.IGNORECASE)

if __name__ == "__main__":
    main()