#!/usr/bin/env python3
import argparse
from big_number import bign


def total(
    galleons: int | float = 0, sickles: int | float = 0, knuts: int | float = 0
) -> float:
    """
    :param galleons: The number of galleons
    :param sickles: The number of sickles
    :param knuts: The number of knuts

    :type galleons: int | float
    :type sickles: int | float
    :type knuts: int | float

    :return: The total amount in knuts with formula
    :rtype: float
    """
    return float((galleons * 3 + sickles) * 5 + knuts)


def main():
    # coins = [100, 50, 75]

    coins = {"galleons": 100, "sickles": 50, "knuts": 75}

    # that is(*coins) "unpacking"
    # one star unpacing list and tuples
    # two star unpacking dicts
    total_knuts = total(**coins)
    print(f"{bign(total_knuts, rounded=False)} knuts")


if __name__ == "__main__":
    main()
