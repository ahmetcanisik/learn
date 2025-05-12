import argparse


class Cat(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(description="Meow like a cat")
        super().add_argument("-n", default=1, help="number of times to meow", type=int)
        self.args = super().parse_args()
        self.meows(self.args.n) if self.args.n > 0 else print("meow")

    def meows(self, times):
        for _ in range(times):
            print("meow")


if __name__ == "__main__":
    Cat()
