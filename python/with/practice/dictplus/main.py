#!/usr/bin/env python
import re

def list_to_dict(l: list) -> dict:
    obj = {}
    for i, e in enumerate(l):
        obj[i] = e
    return obj


def str_to_list(s: str) -> list:
    matches = re.search(r"\[\s?(.+)\s?\]", s)
    
    if matches:
        return [v.strip() for v in matches.group(1).split(",")]
    
    return [v.strip() for v in s.split(",")]
        
def main():
    up = input("Input: ").strip()
    print(list_to_dict(str_to_list(up)))

if __name__ == "__main__":
    main()