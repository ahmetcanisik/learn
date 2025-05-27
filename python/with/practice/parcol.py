#!/usr/bin/env python
from re import fullmatch as re_fullmatch

class Parcol:
    def __init__(self):
        ...
        
    def pit(self, pattern: str):
        matches = re_fullmatch(r"^(\([bg,]{1,3}\))\s?(.+)", pattern)
        
        if not matches:
            raise ValueError("Invalid pattern format!")
        
        mods, text = matches.groups()
        
        if "," in mods and "," not in [mods[0], mods[-1]]:
            for mod in mods.replace(r"^\(", "").replace(r"^(?:.+)\)", "").split(","):
                print(mod)
                
        match mods:
            case ["g", "g"]:
                return text
            case _:
                print("Parcol mods are not found!")

def main():
    parcol = Parcol()
    
    print(parcol.pit("(b,g) text"))

if __name__ == "__main__":
    main()