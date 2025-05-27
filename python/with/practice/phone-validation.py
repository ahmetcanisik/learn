#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def main():
    prompt = input("Phone number: ").strip()
    matches = re.match(r"^\+?(\d{2})?\s?([\d\s]{10,})$", prompt)
    if matches:
        country_code = matches.group(1)
        phone_number = matches.group(2)
        
        print(f"Country code: {country_code if country_code else 'None'}")
        print(f"phone number is {phone_number}")
        
    
if __name__ == "__main__":
    main()