#!/usr/bin/env python3
import csv

def main():
    choice = 1
    print("type 1 for listing user\ntype 2 for adding user\n")
    
    while True:    
        try:
            choice = int(input("List or Add new user? ").strip())
        except Exception:
            continue
        
    
        match choice:
            case 1:
                students = get_users_for_csv("hogwarts_students.csv")
                list_users(students)
                break
            case 2:
                username = input("What's your name? ")
                home = input("Where is your home? ")
                house = input("Where is your house? ")
                
                add_user("hogwarts_students.csv", {
                    "name": username,
                    "home": home,
                    "house": house
                })
                break

def get_users_for_csv(filepath: str = None) -> list:
    
    if filepath is None:
        raise ValueError("Plese specify the file path!")
    
    students = []
    
    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    
    return students
        

def list_users(users: list = []):
    for user in sorted(users, key=lambda user: user["name"]):
        print(f"{user["name"]} is from {user["home"]}")


def add_user(filepath: str = None, user: dict = None):
    
    if filepath is None:
        raise ValueError("Plese specify the file path!")
    
    if user is None:
        raise ValueError("Plese specify the user!")
    
    with open(filepath, "a+") as file:
        """
        writer = csv.writer(file)
        
        writer.writerow([user["name"],user["home"],user["house"]])
        """
        
        writer = csv.DictWriter(file, fieldnames=["name", "home", "house"])
        writer.writerow(user)
        
        print(f"Welcome to new user {user["name"]}!")
    
if __name__ == "__main__":
    main()