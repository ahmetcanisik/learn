#!/usr/bin/env python3
"""i = 3

while i != 0:
    print("meow")
    i -= 1

for _ in range(3):
    print("meow")

for y, z in enumerate(["a", "b", "c", "d"]):
    print(y,z)

print("meow\n" * 3, end="")
"""

def main():
    number = get_number_from_the_user()
    meow_to_screen(number)


def get_number_from_the_user():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow_to_screen(n):
    for _ in range(n):
        print("meow")

if __name__ == "__main__":
    main()