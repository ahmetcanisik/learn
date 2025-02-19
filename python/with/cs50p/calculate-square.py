#!/usr/bin/env python
def main():
    num = input("What's your number? ")
    
    try:
        if isinstance(int(num), int):
            print(f"{num} square is {square(int(num))}")
    except:
        if isinstance(type(num), int) == False:
            print(f"type of {type(num)} is not integer!")
    
    
def square(number: int) -> int:
    if isinstance(number, int):
        return number ** 2 # like this number * number or pow(number, 2)
    
    raise TypeError(f"type of {type(number)} is not integer!")
    
    
if __name__ == "__main__":
    main()