#!/usr/bin/env python3
from rich import print

houses = [
    {"name": "Gryffindor", "color": "red"},
    {"name": "Hufflepuff", "color": "yellow"},
    {"name": "Ravenclaw", "color": "blue"},
    {"name": "Slytherin", "color": "green"},
]

# List of students with their respective houses
students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]


def main():
    for student in students:
        if student["house"] == "Gryffindor":
            print(f"[bold red]{student['name']} is in Gryffindor![/bold red]")
        elif student["house"] == "Hufflepuff":
            print(f"[bold yellow]{student['name']} is in Hufflepuff![/bold yellow]")
        elif student["house"] == "Ravenclaw":
            print(f"[bold blue]{student['name']} is in Ravenclaw![/bold blue]")
        elif student["house"] == "Slytherin":
            print(f"[bold green]{student['name']} is in Slytherin![/bold green]")
        else:
            print(f"[bold white]{student['name']} is in an unknown house![/bold white]")
    print(
        "\n[bold magenta]All students have been sorted into their houses![/bold magenta]"
    )


if __name__ == "__main__":
    main()
