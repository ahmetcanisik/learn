#!/usr/bin/env python3
import re

def main():
    email = input("What's your email? ").strip()
    
    if re.search(r"^[\w\.]@[a-zA-Z0-9\.-]+\.[a-zA-Z0-9]{2,}$", email, re.IGNORECASE):
        print("Valid")
    else:
        print("Invalid")
    
if __name__ == "__main__":
    main()
    
"""
# without re


def is_valid_email(email: str = None) -> bool:
    if email is None:
        raise ValueError("please specify the email address!")
    
    if "@" in email.strip():
        username, domain = email.split("@")
        
        if username and domain.endswith(".com"): # or "." in domain
            return True
    
    return False

"""