#!/usr/bin/env python3
import re

def format_name(name: str | None = None) -> str:
    
    if name is None or not name:
        raise ValueError("Please specify the name for formatting!")
    
    if matches := re.search(r"^(.+)\, *(.+)$", name.strip()):
        last = matches.group(1).strip()
        first = matches.group(2).strip()
        return f"{first}, {last}"
    
    return name

def main():
    name = input("What's your name? ").strip()
    fname = format_name(name)
    
    print(f"Hello, {fname}")

if __name__ == "__main__":
    main()