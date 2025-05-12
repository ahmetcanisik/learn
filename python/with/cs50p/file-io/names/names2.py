names = []
longest_name = 0

for _ in range(3):
    name = input("What's your name? ")
    name_length = len(name)

    if name_length > longest_name:
        longest_name = name_length

    names.append(name)

with open("names.txt", "w", encoding="utf-8") as file:

    file.write(f"names list!\n{"-" * longest_name}\n")

    for i, name in enumerate(sorted(names)):
        file.write(f"{i+1} {name}\n")
