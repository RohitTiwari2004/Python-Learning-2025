#Inheritence
#allows one class (child) to reuse the prop and methods of another class (parents).
#parent class

class student:
    def __init__(self, name, grade, percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage
    def student_details(self): #method
        print(f"{self.name} is in class {self.grade}, with {self.percentage}")

# object - instance of class
student_1 = student('Susmita',11,76)
student_2 = student('Krishna', 12, 84)

#child class

class GraduateStudent(student): #Graduate Student child class inherit prop and method from Student Parent Class 
    def __init__(self, name, grade, percentage,stream ): # old parameters from parent class and new parameters in child class
        super().__init__(name, grade, percentage) #call the parent class init
        self.stream = stream  #new attribute in child class 
    
    def student_details(self):
        super().student_details () #method inherit from parent class
        

#object -- instance of class
Grad_Student1 = GraduateStudent('Keshav',12, 93, 'BCA')
print(Grad_Student1.stream)
print(student_1.percentage)

Grad_Student1.student_details()