#!/usr/bin/env python
from os import system
from time import sleep

def main():
    n = int(input("What's n? "))
    for i, s in enumerate(sheep(n)):
        if i == 0:
            continue
        sleep(1)
        system("clear")
        print(s, end=f"\nsheep: {i}")
        
def sheep(n):
    for i in range(n):
        yield "🐑" * i
        
if __name__ == "__main__":
    main()