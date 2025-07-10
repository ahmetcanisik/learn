from getter import get_positive_int

def gauss(a: int, n: int, d: int):
    # Sn = n/2 * (2a + (n-1) * d)
    sn = n / 2 * (2 * a + (n - 1) * d)

    return sn


def main():
    frm = get_positive_int("From: ", include_zero=True)
    to = get_positive_int("To: ", include_zero=True)
    d = get_positive_int("Step: ", include_zero=True)

    n = gauss(frm, to, d)
    print(f"{frm}+...+{to} with step {d} is: {n}")



if __name__ == "__main__":
    main()