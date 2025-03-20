#!/usr/bin/env python3
def main():
    email = input("What's your email? ").strip()

def is_valid_email(email: str = None) -> bool:
    if email is None:
        raise ValueError("please specify the email address!")
    
    if "@" in email:
        return True
    
    return False

if __name__ == "__main__":
    main()