#!/usr/bin/env python3
def main():
    hello("world")
    goodbye("world")

def hello(name: str):
    print("Hello, ", name)
    
def goodbye(name: str):
    print("Goodbye, ", name)

if __name__ == "__main__":
    main()