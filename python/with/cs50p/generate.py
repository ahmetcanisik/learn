#!/usr/bin/env python3
import random

USERS = []

def main():
    ask_user_info()
    shuffle_users()
    print("The winner is " + choose_winner())


def choose_winner():
    return random.choice(USERS)

def shuffle_users():
    random.shuffle(USERS)

def ask_user_info():
    for _ in range(3):
        name = input("What's your name? ")
        if name is not None:
            USERS.append(name)
    

if __name__ == "__main__":
    main()