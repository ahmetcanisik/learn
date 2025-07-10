def get_string(m: str = None) -> str:
    while True:
        try:
            s = input(m).strip()
            if s:  # Check if string is not empty
                return s
            else:
                print("Please enter a non-empty string.")
        except (ValueError, TypeError):
            print("Invalid input. Please try again.")
            continue


def get_int(m: str = None) -> int:
    while True:
        try:
            n = int(input(m).strip())
            return n  # If int() succeeds, we have a valid integer
        except ValueError:
            print("Not a number!")
            continue


def get_positive_int(m: str = None, include_zero=False) -> int:
    while True:
        n = get_int(m)
        if n > (-1 if include_zero else 0):
            return n
        else:
            print("Not positive integer!")


def get_negative_int(m: str = None, include_zero=False) -> int:
    while True:
        n = get_int(m)
        if n < (1 if include_zero else 0):
            return n
        else:
            print("Not negative integer!")