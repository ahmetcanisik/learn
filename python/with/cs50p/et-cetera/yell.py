#!/usr/bin/env python
def main():
    yell("Hello", "from", "University", "of", "Harran")


def yell(*words) -> None:
    """
    uppercased: list[str] = []

    for word in words:
        uppercased.append(word.upper())
    """

    upper = [
        word.upper() for word in words
    ]  # map(str.upper, words) >--< map(lambda word: word.upper(), words)
    print(*upper)


if __name__ == "__main__":
    main()
