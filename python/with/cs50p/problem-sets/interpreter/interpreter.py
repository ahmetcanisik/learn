import re

prompt = input("Expression: ").strip().lower()
matches = re.fullmatch(r"^([\d-]+)\s?([\+\-\*\/])\s?([\d-]+)$", prompt)

if matches:
    x, y, z = matches.groups()  # Destructure the groups directly
    x, z = float(x), float(z)  # Convert x and z to float

    match y:
        case "+":
            print(x + z)
        case "-":
            print(x - z)
        case "*":
            print(x * z)
        case "/":
            print(x / z)
        case _:
            print("Invalid operator")
else:
    print("Invalid expression")
