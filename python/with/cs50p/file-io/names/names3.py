def write_file(file_name, content):
    with open(file_name, "w") as f:
        f.write(content)

def add_line_number(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    
    with open(file_name, "w") as f:
        for i, line in enumerate(lines):
            f.write(f"{i+1} {line}")  # Satır numarası ekleyerek yaz

add_line_number("names.txt")