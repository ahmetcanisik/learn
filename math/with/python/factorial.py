from getter import get_positive_int

# n! = (n - 1) * n
def factorial(n: int):
    r = 1
    # ex: n = 3, 1 * 1, 2 * 1, 3 * 2
    for i in range(n):
        r *= (i+1)
    return r


def main():
    n = get_positive_int("n: ", include_zero=True)
    print(f"{n}! = {factorial(n)}")


if __name__ == "__main__":
    main()