#!/usr/bin/env python3
import json
import os
from PyPDF2 import PdfReader
import re


def clean_student_data(text):
    # Remove location and faculty information
    locations = [
        "AKÇAKALE",
        "BİRECİK",
        "BOZOVA",
        "CEYLANPINAR",
        "EYYÜBİYE",
        "HALFETİ",
        "HALİLİYE",
        "HARRAN",
        "HİLVAN",
        "KARAKÖPRÜ",
        "SİVEREK",
        "SURUÇ",
        "VİRANŞEHİR",
    ]
    faculty_terms = ["FAKÜLTESİ", "MESLEK", "YÜKSEKOKULU"]

    # Remove locations and faculty terms from the text
    for loc in locations:
        text = text.replace(loc, "")
    for term in faculty_terms:
        text = text.replace(term, "")

    # Remove extra spaces and return cleaned text
    return " ".join(text.split())


def extract_student_data(pdf_path):
    reader = PdfReader(pdf_path)
    students = []

    for page in reader.pages:
        text = page.extract_text()
        # Look for patterns like "242325013 YUNUS EMRE ALAGÖZ"
        pattern = r"(\d{9})\s+([A-ZĞÜŞİÖÇ\s]+[A-ZĞÜŞİÖÇ])"
        matches = re.finditer(pattern, text)

        for match in matches:
            student_id = match.group(1)
            full_name = clean_student_data(match.group(2))

            # Split the cleaned name into parts
            name_parts = full_name.split()
            if len(name_parts) >= 2:
                surname = name_parts[-1]
                name = " ".join(name_parts[:-1])

                students.append(
                    {"id": student_id, "name": name.strip(), "surname": surname.strip()}
                )

    return students


def update_users_json(new_students):
    # Read existing users
    try:
        with open("data/users.json", "r", encoding="utf-8") as f:
            existing_users = json.load(f)
    except FileNotFoundError:
        existing_users = []

    # Create a set of existing IDs for quick lookup
    existing_ids = {user["id"] for user in existing_users}

    # Add only new students
    for student in new_students:
        if student["id"] not in existing_ids:
            existing_users.append(student)
            existing_ids.add(student["id"])

    # Write back to file
    with open("data/users.json", "w", encoding="utf-8") as f:
        json.dump(existing_users, f, ensure_ascii=False, indent=2)


def extract_student_numbers(pdf_path):
    reader = PdfReader(pdf_path)
    student_numbers = set()  # Using set to automatically handle duplicates

    for page in reader.pages:
        text = page.extract_text()
        # Look for 9-digit student numbers
        matches = re.finditer(r"(\d{9})", text)
        for match in matches:
            student_number = match.group(1)
            student_numbers.add(student_number)

    return student_numbers


def save_student_numbers(numbers):
    # Sort numbers before saving to make output consistent
    sorted_numbers = sorted(numbers)

    # Save to txt file
    with open("student_numbers.txt", "w", encoding="utf-8") as f:
        for number in sorted_numbers:
            f.write(f"{number}\n")


def main():
    # Process all PDF files
    pdf_files = [
        f
        for f in os.listdir(".")
        if f.startswith("ogrenci_yerleri_listesi") and f.endswith(".pdf")
    ]

    # Using set for all numbers to prevent duplicates
    all_numbers = set()

    for pdf_file in pdf_files:
        print(f"Processing {pdf_file}...")
        numbers = extract_student_numbers(pdf_file)
        # Union of sets to avoid duplicates
        all_numbers.update(numbers)

    # Save to file
    save_student_numbers(all_numbers)
    print(f"Total unique student numbers saved: {len(all_numbers)}")
    print("Numbers saved to student_numbers.txt")


if __name__ == "__main__":
    main()
