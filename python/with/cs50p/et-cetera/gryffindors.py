students = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

"""
# list method
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]
"""

"""
# function method
def is_gryffindor(s):
    return s["house"] == "Gryffindor"
    
filter(is_gryffindor, students)
"""

# filter method
filtered = filter(lambda student: student["house"] == "Gryffindor", students)

for student in sorted(filtered, key=lambda student: student["name"]):
    print(f"{student["name"]} is in Gryffindor")
