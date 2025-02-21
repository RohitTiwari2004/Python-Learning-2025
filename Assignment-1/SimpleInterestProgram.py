#write a program to find simple interest of the given inputs. 

principal= int(input("enter the principal amount\n"))
time= float(input("enter the time taken"))
rate= float(input("enter the rate"))

SI=(principal*time*rate)/100
print("the SI is",SI)


