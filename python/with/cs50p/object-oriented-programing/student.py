#!/usr/bin/env python3

class Student:
    def __init__(self, name, house, patronus):
        self.name = name
        self.house = house
        self.patronus = patronus
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
        
    @property
    def patronus(self):
        return self._patronus
    
    @patronus.setter
    def patronus(self, patronus):
        if not patronus:
            raise ValueError("Missing patronus")
        self._patronus = patronus
    
    # Getter
    @property
    def house(self):
        if not self._house:
            raise ValueError("Missing house")
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        
        self._house = house
    
    def __str__(self):
        return f"{self._name} from {self._house}"
        

def main():
    student = get_student()
    student.name = "Ron"
    print(student)

def get_student(name: str = None, house: str = None, patronus: str = None):
    if not name:
        name = input("Enter name: ")
    if not house:
        house = input("Enter house: ")
    if not patronus:
        patronus = input("Enter patronus: ")
    
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()