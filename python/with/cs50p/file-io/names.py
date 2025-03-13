names = []

def hello(to="world"):
    return f"Hello, {to}"

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(hello(name))