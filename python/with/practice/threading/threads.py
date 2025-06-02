#!/usr/bin/env python
import threading
import time
import json
import os

def get_users():
    users = []
    with open("users.json", "r", encoding="utf-8") as file:
        users = json.load(file)
    return users

def list_users():
    users = get_users()

    for i, user in enumerate(users):
        print(f"{i+1}. {user}")

def wait(for_second: int = 10) -> bool:
    for i in range(for_second):
        j = for_second - i
        print(f"program, {j} saniye sonra duracak.")
        time.sleep(j)
    
    return True


def main():
    timer = threading.Thread(target=wait)

    timer.start()

    while timer.is_alive():
        os.system("clear")
        list_users()
        time.sleep(1)


if __name__ == "__main__":
    main()