#!/usr/bin/env python3
from rich import print

students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]


def main():
    global houses
    houses = set()

    for student in students:
        houses.add(student["house"])

    for house in sorted(houses):
        print(f"[bold blue]{house}[/bold blue]")


if __name__ == "__main__":
    main()
