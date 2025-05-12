#!/usr/bin/env python3


def main():
    ternary("5 == 5 ? is equal : is not equal")


def ternary(c: str = None):
    if c is not None:
        c = c.strip()

        # get conditions and expression
        condition, expression = c.split("?")

        # split to condition(true or false line.)
        is_condition_true, is_condition_false = expression.strip().split(":")

        ternary_check(condition, ["==", "!="], is_condition_true, is_condition_false)


def ternary_check(
    condition: str = None,
    cons: list[str] = None,
    is_true: str = None,
    is_false: str = None,
):
    for con in cons:
        if condition.index(con):
            l, r = condition.split(con)
            if l.strip().lower() == r.strip().lower():
                print(is_true)
            else:
                print(is_false)


if __name__ == "__main__":
    main()
