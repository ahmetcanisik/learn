#!/usr/bin/env python3
from rich import print
import re

"""
Make money to readable for human.

prompts;
- money: integer or float or string values.

returning readable money is string.
"""


def mmr(money: int | float | str) -> str:
    if not money:
        raise ValueError("Missing money")

    try:
        fmoney = float(money)
    except ValueError:
        raise ValueError("Invalid money value")

    return "{:,.2f}".format(fmoney)


def main():
    print(
        """
        help: Turkish lira to Dollar converter.
        """
    )
    tl = float(input("Enter 'Turkish Lira' amount: "))
    dollars = tl / 40
    print(f"{mmr(tl)}₺ is {mmr(dollars)}$")


if __name__ == "__main__":
    main()


"""
add rich with version to requirements.txt
python3 -c "import subprocess;import re; spkg = subprocess.run(['pip', 'list'], capture_output=True, text=True).stdout; rich_i = re.search(r'rich\s(.+)', spkg, re.IGNORECASE).group(0); print(rich_i.replace(r' ', '').replace('h', 'h>='))" >> requirements.txt
"""
