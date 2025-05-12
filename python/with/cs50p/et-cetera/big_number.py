def bign(n: int | float = 0, rounded=True) -> str | None:
    THOUSAND = 1000
    MILLION = 1000000
    BILLION = 1000000000
    TRILLION = 1000000000000

    n = float(n)
    nl = "{:,.2f}".format(n)
    ns = nl.split(",")[0]

    match n:
        case n if n < 0:
            return None
        case n if n < THOUSAND:
            return nl
        case n if n == THOUSAND:
            return f"a thousand" if rounded else nl
        case n if n >= THOUSAND and n < MILLION:
            return f"{ns}k" if rounded else nl
        case n if n == MILLION:
            return f"a million" if rounded else nl
        case n if n >= MILLION and n < BILLION:
            return f"{ns}m" if rounded else nl
        case n if n == BILLION:
            return f"a billion" if rounded else nl
        case n if n >= BILLION and n < TRILLION:
            return f"{ns}b" if rounded else nl
        case n if n == TRILLION:
            return f"a trillion" if rounded else nl
        case n if n >= TRILLION:
            return f"{ns}t" if rounded else nl
        case _:
            return None
