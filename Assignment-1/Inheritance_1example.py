#example
class company:
    def __init__(self,name,products,yearexperience):
        self.name = name
        self.products = products
        self.yearexperience = yearexperience
    def company_details(self): #method
        print({self.name},{self.products},{self.yearexperience})
#Object -- instance of class
Company_1 = company('Surya Private Limited', 'General', 25)
Company_1.company_details()

#child class

class smallcompany(company):
    def __init__(self,name,products, yearexperience,technology):
        super().__init__(name,products,yearexperience)
        self.technology = technology
smallcompany_1 = smallcompany('Royal_Furniture','Furnitures',28, 'New machines')
print(smallcompany_1.__dict__)
print(smallcompany_1.name)






