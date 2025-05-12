import argparse

parser = argparse.ArgumentParser(description="Hello to you")
parser.add_argument("-n", default=None, help="Enter your full name", type=str)
args = parser.parse_args()

first, _ = (
    args.n.split(" ")
    if args.n is not None
    else input("What's your name? ").strip().split(" ")
)

print(f"Hello, {first}")
