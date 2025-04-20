#Encapsulation
class Student:
    def __init__(self,name,grade, percentage):
        self.name = name
        self.grade = grade
        self.__percentage = percentage 
    
    def Student_details(self):
        print({self.name}, {self.grade}, {self.__percentage})

Student_1 = Student('Roshan',11, 87)
print(Student_1.name)
# print(Student_1.__percentage)
# Student_1.__Student_details()

class volunteer:
    def __init__ (self,name,skill, age):
        self.name = name
        self.__skill = skill
        self.age = age
    def volunteer_details(self):
        print({self.name},{self.__skill},{self.age})
volunteer_1 = volunteer('Susmita', 'Volunteering', 23)
print(volunteer_1.name)
print(volunteer_1.__skill)
volunteer_1.volunteer_details()