students = []

with open("hogwarts_students.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({
            "name": name,
            "house": house
        })
    

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['house']}")