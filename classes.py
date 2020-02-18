class Student:
    name = "student"
    def __init__(self, name, age, class_):
        self.name = name
        self.age = age
        self.class_ = class_
    
    def average(self, x, y, z):
        return (x+y+z)/3

james = Student("James",15,"9C")

print(james.average(5,10,15))