num= int(input('enter any three digit number\n'))
#345%10 =5
a= num%10
num=num//10

#34%10 =4
b=num%10
num=num//10

# 3%10 =3
c=num%10
num=num/10 
print(a+b+c)