#!/usr/bin/env python
from sys import argv
from commands import command_list

def list_commands():
    for cmd in command_list:
        print(f"- {", ".join(cmd['args']) if isinstance(cmd["args"], list) else str(cmd["args"])}")

def main():
    if len(argv) > 1:
        for command in command_list:
            if argv[1] in command["args"]:
                print("\n==> Running...", command["name"].title(), end="\n\n")
                if "print" in command and command["print"]:
                    print(command["print"])
                if "execute" in command and command["execute"]:
                    command["execute"]()
                if command["name"] == "Help":
                    list_commands()

                # If flags are containing and list is not empty
                if "options" in command and command["options"]:
                    for option in command["options"]:
                        if option["option"] in argv:
                            option["run"]()
                return

    print(f"\n{", ".join(argv[1:])} Command not found!\n\nHere is command list:")
    list_commands()

if __name__ == "__main__":
    main()