#!/usr/bin/env python3
from os import system as os_system

def main():  
    x = 0
    while True:
        try:
            os_system("clear")
            x = int(input("What's x? "))
        except ValueError:
            continue
        
        break
    print(f"{x} square is {square(x)}")


def square(n):
    return n * n

if __name__ == "__main__":
    main()