#Polymorphism 
class student:
    def __init__(self, name, grade, percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage
    def student_details(self): #method
        print(f"{self.name} is in class {self.grade}, with {self.percentage}")

# object - instance of class
student_1 = student('Susmita',11, 76)
student_2 = student('Krishna', 12, 84)

#Child Class

class GraduateStudent(student): 
    def __init__(self, name, grade, percentage,stream ): 
        super().__init__(name, grade, percentage)
        self.stream = stream  #new attribute in child class 
    
    def student_details(self):
        print(f'{self.name} is in class{self.grade}, with {self.percentage} and from {self.stream   }')
#object for student class
student_1 = student('Susmita',11,76)

# object for Graduate student class
Grad_Student1 = GraduateStudent('Keshav',12, 93, 'BCA')

student_1.student_details()
Grad_Student1.student_details()