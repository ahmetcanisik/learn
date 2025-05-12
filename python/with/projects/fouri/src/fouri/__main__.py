#!/usr/bin/env python3
from fouri.find import find_dizipal
from fouri import get_commands
from sys import argv


def main():
    if len(argv) == 1:
        find_dizipal()
        exit()

    if len(argv) == 2:
        commands = get_commands()

        for command in commands:
            if argv[1] in command["flags"]:
                print(command["fn"]())
                exit()

    print(f"command not found {" ".join(argv[1:])}")


if __name__ == "__main__":
    main()
