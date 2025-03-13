#!/usr/bin/env python3

def main():
    student = Student()
    student.list_students()
    

class Student:
    def __init__(self):
        self.students = [
            {
                "name": "Hermione",
                "house": "Gryffindor",
                "patronus": "Otter"
            },
            {
                "name": "Harry",
                "house": "Gryffindor",
                "patronus": "Slag"
            },
            {
                "name": "Ron",
                "house": "Gryffindor",
                "patronus": "Jack Russel terrier"
            },
            {
                "name": "Malfoy",
                "house": "Slytherin",
                "patronus": None
            }
        ]
    
    def new_student(self):
        name = input("What's your name? ")
        house = input("Where is your house of Hogwarts? ")
        patronus = input("Your patronus? ")
        self.save_student({
            "name": name,
            "house": house,
            "patronus": patronus
        })

    def save_student(self, student):
        self.students.append(student)
        
    def list_students(self):
        print("The Patronus of Students in Hogwarts!")
        for i, student in enumerate(self.students): # range(leng(self.students))
            print(f"{i+1}. {student["name"]} from {student["house"]} has {student["patronus"]}")
    
    def get_students(self) -> list:
        return self.students
        
if __name__ == "__main__":
    main()