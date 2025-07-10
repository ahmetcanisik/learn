import re


def square(n: int) -> int:
    return n * n


def absolute_value(val: int) -> int:
    vals = str(val)

    if (matches := re.match(r"\s*-([\d]+)\s*", vals)):
        print("negative number detected!")
        return int(matches.group(1))
    
    return val
    


def get_absolute_value() -> None:
    n = int(input("Absolute value: "))
    print(f"|{n}| = {absolute_value(n)}")


def get_square() -> None:
    n = int(input("Number of square: "))
    print(f"{n} square is {square(n)}")


def welcome_message():
    print("Welcome to the mathf! Choice your process and continue...\n\nKey\t| Process\n----\t|----")
    list_processes()


def list_processes():
    keys = [
        {
            "key": '1',
            "process": "square of the number"
        },
        {
            "key": '2',
            "process": "absolute value of the number"
        }
    ]
    
    
    for key in keys:
        print(f"{key['key']}\t| {key['process']}")



def get_choice():
    choice = input("\nWhat do you want? ")
    
    match choice:
        case '1':
            get_square()
        case '2':
            get_absolute_value()
        case _:
            print("Invalid choice.")
            return


def main():
    welcome_message()
    
    while True:
        try:
            get_choice()
        except ValueError:
            print("That's not an number!")
            continue
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()