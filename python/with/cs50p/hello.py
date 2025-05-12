"""
def say(*values: object):
    print(values)

say("+ What's your name?")
"""


def capitalizeName(value: str | list[str]) -> str:
    if not isinstance(value, str) and not isinstance(value, list[str]):
        raise TypeError(
            f"Are Expected types of value is str or list[str] but not {type(value)}"
        )

    nam = value.split(" ") if isinstance(value, str) else value
    un = ""
    for i, n in enumerate(nam):
        un += f"{n.capitalize()}{"" if len(nam[i]) == (len(nam) - 1) else " "}"

    return un


print("Start the", end=" ")
print("Conversation...")

print("+ What's your name?")
name = input("- My name is ").strip()

# Use capitalizeName or string.title() method. They both are same.
print(f"+ Hello, {name.title()}")
