students = ["Harry", "Hermione", "Ron", "Neville", "Ginny", "Luna", "Fred", "George", "Lee", "Angelina", "Katie", "Alicia"]

#gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)