#!/usr/bin/env python3
import re

def main():
    email = input("What's your email? ").strip()
    
    if is_valid_email(email):
        print("That is a Valid email address!")
    else:
        print("is not valid email address!")


def is_valid_url(url: str = None) -> bool:
    
    if url is None:
        raise ValueError("please specify the url address")
    
    if re.search(r"^(https?)://[\w-]+\.\w{2,4}$", url, re.IGNORECASE):
        return True
    
    return False

    
def is_valid_email(email: str = None) -> bool:
    
    if email is None:
        raise ValueError("please specify the email address!")
    
    if re.search(r"[\w\._-]+@([\w-]+\.)+[\w-]{2,63}", email): # [a-zA-Z0-9] is equal to \w
        return True
    
    return False
    
if __name__ == "__main__":
    main()