#!/usr/bin/env python3
import os

"""
read .py files and find three quotes texts. and convert this file to .md
then create docs folder and put the .md file in it.
"""


# First, read all .py files.
def read_py_files():
    py_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files


# Second, find three quotes texts.
def find_quotes(py_files):
    quotes = []
    for file in py_files:
        with open(file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('"""') or line.startswith("'''"):
                    quotes.append(line.strip())
    return quotes


# Third, convert this file to .md
def convert_to_md(quotes):
    md_content = "# Quotes\n\n"
    for quote in quotes:
        md_content += f"> {quote}\n\n"
    return md_content


# Fourth, create docs folder and put the .md file in it.
def create_docs_folder(md_content):
    if not os.path.exists("docs"):
        os.makedirs("docs")
    with open("docs/quotes.md", "w", encoding="utf-8") as f:
        f.write(md_content)


# Main function
def main():
    py_files = read_py_files()
    quotes = find_quotes(py_files)
    md_content = convert_to_md(quotes)
    create_docs_folder(md_content)
    print("Quotes have been extracted and saved to docs/quotes.md")


if __name__ == "__main__":
    main()
