def meow(n: int) -> list[str]:
    meows = ["meow" for _ in range(n)]
    print("\n".join(meows))
    return meows


times: int = int(input("Number of meows: "))
meows: list[str] = meow(times)
print(", ".join(meows))

"""
test yapabiliyorum pytest ile,
tip kontrolü yapabiliyorum mypy ile,
docstring ile detaylı açıklamalar ekleyebiliyorum
"""
