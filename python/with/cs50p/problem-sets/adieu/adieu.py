class Adieu:
    def __init__(self):
        self.prefix = "Adieu, adieu, to "

    def say(self, *to: str) -> str:
        # prefix
        p = self.prefix

        l = len(to)

        if l == 1:
            return f"{p}{to[0]}"

        return f"{p}{", ".join(to[:-1])}, and {to[-1]}"

        return p


def main():
    adieu = Adieu()
    names = []
    
    while True:
        try:
            name = input("Name: ").strip()

            names.append(name)
        except EOFError:
            break

    print(adieu.say(*names))


if __name__ == "__main__":
    main()