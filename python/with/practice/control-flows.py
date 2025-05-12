#!/usr/bin/env python3
for number in list(range(2, 10, 2)):
    print(number * 2)

print(sum(range(4)))  # 0 + 1 + 2 + 3

match (5, 3):
    case (1, 2):
        print(f"x is 1 and y is 2")
    case (x, 3):
        print(f"x is {x} and y is 3")
    case _:
        raise ValueError("not a point!")


def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        reply = input(prompt)
        if reply in {"y", "ye", "yes"}:
            return True
        if reply in {"n", "no", "nop", "nope"}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)


if __name__ == "__main__":
    ask_ok("Do you want a gift? ")
