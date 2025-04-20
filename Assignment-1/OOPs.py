#using list
Student_1 =["Shukla", "Mohit"]
print(f"Hey,{Student_1[0]}")

# using OOPs - creating student records

# class Student:
#     name = 'Rohit'
#     Grade = 13
# Student1 = Student()
# print(Student1.name)

class Student:
    def __init__(self,Full_Name,Class_Grade):
        self.Name = Full_Name
        self.Grade = Class_Grade
Student_1 = Student('Rohit',13)
print(Student_1.Name, Student_1.Grade)

Student_2 = Student('Mohit', 11)
print(Student_2.Name, Student_2.Grade)

class Teacher:
    def __init__(self,full_name,salary):
        self.name = full_name
        self.salary = salary
Teacher_1 = Teacher('Shriyansh', 24000)
print(Teacher_1.name, Teacher_1.salary)

class Accountant:
    def __init__(self,Accountant_name,Accountant_Salary):
        self.name = Accountant_name
        self.Salary = Accountant_Salary

Employee = Accountant('Rohit',25000)
print(Employee.name, Employee.Salary)

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
student_1 = Student('Rohan',78)
print(f"{student_1.name} has got {student_1.marks} in Exam")
print(student_1.__dict__)
del student_1.name
print(student_1.__dict__)

#Lets suppose, if we want to delete the object

# del student_1
# print(student_1)