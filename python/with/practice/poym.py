#!/usr/bin/env python3


class Poym:
    def __init__(self, firstPrompt: str = None):
        self.chatHistory = []

        if firstPrompt is not None:
            self.chatHistory.append({"role": "user", "content": firstPrompt})

    """
    Talk with POYM
    """

    def talk(self, prompt: str = None):
        if prompt is None:
            raise ValueError("Missing prompt")

        ...


def main(): ...


if __name__ == "__main__":
    main()
