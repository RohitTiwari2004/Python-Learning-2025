#Write a program to find the length of given string without using len function

S=input('Enter the String\n')
count=0

for i in S:
    count+=1

print('The length of string is',count)


#Program to find the length of string using len function

SR= input('Enter the String\n')
string_length= len(SR)
print('the length of string is',string_length)