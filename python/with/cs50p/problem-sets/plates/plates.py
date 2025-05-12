#!/usr/bin/env python
import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    re.match(r"", s)


if __name__ == "__main__":
    main()
