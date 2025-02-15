#!/usr/bin/env python
from sys import argv
from commands import command_list

def main():
    if len(argv) > 1:
        for command in command_list:
            if argv[1] == command["name"]:
                command["run"]()

                # Eğer "flags" anahtarı varsa ve listesi boş değilse
                if "flags" in command and command["flags"]:
                    for flag in command["flags"]:
                        if flag["flag"] in argv:
                            flag["run"]()
                return  # Komut bulunduysa döngüyü sonlandır

    for cmd in command_list:
        print(f"- {cmd['name']}")

if __name__ == "__main__":
    main()