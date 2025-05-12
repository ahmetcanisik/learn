#!/usr/bin/env python3
names = []


def hello(to="world"):
    return f"Hello, {to}"


def main():
    for _ in range(3):
        names.append(input("What's your name? "))

    for name in sorted(names):
        print(hello(name))


if __name__ == "__main__":
    main()
