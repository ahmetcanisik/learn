#!/usr/bin/env python3
def main():
    h = int(input("What is the pyramid height? "))
    pyramid(h)
    #print_square(6)
    
def print_square(size):
    """
    # solution 1
    
    for _ in range(size):
        draw = ""
        for _ in range(size):
            draw += "#"
        print(f"{draw}\n", end="")
    """
    
    # solution 2
    for _ in range(size):
        print_row(size)
        

def pyramid(n):
    for i in range(n):
        print("#" * (i + 1))

def print_row(width):
    print("#" * width)


if __name__ == "__main__":
    main()