#!/usr/bin/env python3

def main():
    match get_student():
        case (name, house) if house.strip().lower() in ['Gryffindor', 'Slytherin', 'Rawenclaw']:
            match name.strip().lower():
                case 'padma' if house == "Gryffindor":
                    print(f"{name} is in Gryffindor")
        case (name, _):
            print(f"{name} isn't a Hogwart student")

def get_student():
    name = input("Enter name: ")
    house = input("Enter house: ")
    return name, house # --> automaticly converting to tuples like this (name, house)

if __name__ == "__main__":
    main()