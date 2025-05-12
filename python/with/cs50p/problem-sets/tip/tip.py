import re


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str = None) -> float:
    if d is None:
        raise ValueError("dollars is missing!")

    try:
        match = re.fullmatch(r"^\$?(\d+(\.\d+)?)$", d)

        if match:
            return float(match.group(1))
    except Exception:
        raise TypeError("dollars is not a number!")


def percent_to_float(p: str = None) -> float:
    if p is None:
        raise ValueError("percents is missing!")

    try:
        match = re.fullmatch(r"^(\d+)\%?$", p)

        if match:
            return float(match.group(1)) / 100
    except Exception:
        raise TypeError("percents is not a number!")


main()
