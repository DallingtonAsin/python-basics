# Object Oriented Programming

class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
    def print_details(self):
        print("\nI am %s, student no: %s and I am %d years old." % (self.name, self.id, self.age))

s = Student("Najib Jama", 22, "4005")
s.print_details()
