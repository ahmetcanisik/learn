import random


def get_level() -> int:
    while True:
        try:
            level = int(input("Level: ").strip())
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue


def generate_integer(level: int) -> int:
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")


def main():
    level = get_level()
    score = 0

    for _ in range(10):  # 10 soru sorulacak
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        attempts = 3

        while attempts > 0:
            try:
                answer = int(input(f"{x} + {y} = ").strip())
                if answer == result:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts -= 1
            except ValueError:
                print("EEE")
                attempts -= 1

        if attempts == 0:
            print(f"{x} + {y} = {result}")

    print(f"Score: {score}/10")


if __name__ == "__main__":
    main()
