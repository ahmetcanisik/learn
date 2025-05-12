from random import randint


def rand(
    # length is generated random characters length, maybe 5, 7 etc. but default zero
    length: int = 0,
    # included numbers to generating random process? default, yes include: True
    numbers: bool = True,
    # included characters to generating random process? default, don't add do this: False
    chars: bool | str = False,
    # included characters to generating random process? default, don't add do this: False
    turkishChars: bool | str = False,
    # including you're specify special characters to generating random process? don't add any special chars: None
    specialChars: str | None = None,
) -> str:

    # r shorted random. this is collected generated random characters.
    r = ""

    # c shorted characters. own upper chars.
    c = "ABCDEFGHIJKLMNOPRSTUVYZXW"

    # t shorted turkish characters. own turkish upper chars.
    t = "ÇĞİÖŞÜ"

    # upper chars
    uc = c if (chars == True or chars == "upper") else ""

    # lower chars
    lc = c.lower() if (chars == True or chars == "lower") else ""

    # numbers
    n = "0123456789" if numbers else ""

    # turkish upper chars
    tu = t if (turkishChars == True or turkishChars == "upper") else ""

    # turkish lower chars
    tl = t.lower() if (turkishChars == True or turkishChars == "lower") else ""

    # special chars
    s = specialChars if specialChars is not None else ""

    # collect all characters
    c = uc + lc + n + tu + tl + s

    for _ in range(length):
        r += c[randint(0, len(c) - 1)]

    return r
