#Write a python program to remove particular character from user given string

user_input = input('Enter the string\n')
term = input('What would you want to remove\n')
result = ''

for i in user_input:
    if i != term:
       result = result+i
print(result)
