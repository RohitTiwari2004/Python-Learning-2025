# Polymorphism
class teacher:
    def __init__(self,name,subject,experience): # attribute
        self.name = name
        self.subject = subject
        self.experience = experience
    def teacher_details(self): #method
        print(f'{self.name} teaches {self.subject} with {self.experience} of experience')
#Object -- instance of class
teacher_1 = teacher('Krishna','Mathematics', 12)
teacher_2 = teacher('Roshni','Sociology', 24)

#child class
class upper_teacher(teacher):
    def __init__(self,name,subject,experience):
        super().__init__(name,subject,experience)

    def teacher_details(self):
        print(f'{self.name} teaches {self.subject} with {self.experience} of experience')
#object - teacher
teacher_1 = teacher('Krishna','Mathematics', 12)
#object -- upper teacher
upperteacher_1 = upper_teacher('Gaurab','Economics',25)

upperteacher_1.teacher_details()
print(teacher_1.__dict__)
del upperteacher_1.name
print(upperteacher_1.__dict__)





