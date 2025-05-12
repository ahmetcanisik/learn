#!/usr/bin/env python3
class Cat:
    MEOW = 3

    def meow(self, times=MEOW):
        for _ in range(times):
            print("Meow")


def main():
    cats = set()

    cats.add("Fasulye")
    cat = Cat()
    cat.meow(3)


if __name__ == "__main__":
    main()
