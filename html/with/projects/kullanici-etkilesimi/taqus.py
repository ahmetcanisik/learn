const = {
    "test": 3,
    "test2": 4,
    "test3": 5
}

for i in [key.upper() for key in const.keys()]:
    print(i)
    