#!/usr/bin/env python3

def main():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not integer")
        else:
            break

    print(f"x is {x}")

if __name__ == "__main__":
    main()