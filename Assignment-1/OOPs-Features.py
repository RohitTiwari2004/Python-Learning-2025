#OOPs Features
#Abstraction - Hiding unnecesary details from users through class, method
#Encapsulation
#Inheritance
#Polymorphism

#SIMPLE EXAMPLE USING ABSTRACTION

class Student:
    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage

    def Student_Details(self): #method
        print({self.name},{self.grade},{self.percentage})

#Object - Instance of Class
Student_1 = Student('Rohit',12,93)
Student_2 = Student('Aabiskar',11,91)

Student_1.Student_Details()
Student_2.Student_Details()

class Teacher:
    def __init__ (self,name,age,grade):
        self.name = name
        self.age = age
        self.__grade = grade
    def get_grade(self):
        return self.__grade
    def Teacher_Details (self):
        print({self.name},{self.age}, {self.grade})
    
Teacher_1 = Teacher ('Roshan', 24, 'A')
# Teacher_1.Teacher_Details()
print(Teacher_1.__grade)
print(Teacher_1.get_grade())

