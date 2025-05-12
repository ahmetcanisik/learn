secili_islem = "toplama"
sayilar = (5, 3)

islemler = {
    "toplama": lambda x, y: x + y,
    "cikarma": lambda x, y: x - y,
    "carpma": lambda x, y: x * y,
    "bolme": lambda x, y: x / y,
}

for islem, isle in islemler.copy().items():
    if islem == secili_islem:
        print(
            f"{str(sayilar).split(",")} için {islem} işleminin sonucu = {isle(sayilar[0], sayilar[1])}"
        )
