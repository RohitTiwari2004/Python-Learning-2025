#File Handling in Python allows you to read from and write to file. This is important whem you want to store data permanently or work with the large datasets.
# Python provides built-in functions and methods to interact with files.
#Steps for File Handling in Python :
#Opening a file
#Reading from a file
#Writing to a file
#Closing the file


#write to a file
file = open('example2.txt', 'w')
#it creates a file if it is does not exist on folder.
file.write('Its been a long day')
file.close()

#append mode
file = open('example2.txt', 'a') #append mode
file.write('\nYeah!, it is')
file.close()

file = open('ShortInfo.txt', 'w')
file.write('Its me Rohit Tiwari')
file.close()

#to add some sentence on ShortInfo.txt, I use append mode
file = open('ShortInfo.txt', 'a') #add incremental value..  
file.write('\nAlways curious to learn new stuffs')
file.close()

#close a file using with statement
with open('ShortInfo.txt', 'r') as file:
 message = file.readlines()
 print(message)

