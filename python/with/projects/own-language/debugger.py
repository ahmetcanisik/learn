"""
language extension: fv

comments like these: >hello from iterators.
"""
import re

def comments(path: str):
    if not path.endswith('.fv'):
        raise ValueError("File must be a .fv file")

    try:
        mc = []
        with open(path, 'r') as file:
            for line in file:
                matches = re.fullmatch(r'>\s?(.*)$', line)
                if matches:
                    mc.append(matches.group(1))
        print(*mc, sep='\n')
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path} not found")
    
def main():
    comments("test.fv")

if __name__ == "__main__":
    main()