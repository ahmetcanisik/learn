def get_n(question: str):
    if question is not None:
        x = int(input("What's x? "))
        return x


x = get_n("What's x? ")
y = get_n("What's y? ")

if x == y:
    print("x equal to y")
else:
    print("x isn't equal to y")
