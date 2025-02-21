    # We see two types of Loop in Python
      #The first one is While Loop
        #The second one is For Loop 

  #rc=int(input('Enter the number:\n'));
 # i=1;
 # while i<11:
 # print(rc*i)
  #i+=1;#

  # guessing game

  # generate a random integer between 1 and 100
import random
rohit=random.randint(1,100)

guess=int(input('Guess any number'))
count=1
while(guess!=rohit):
 if(guess<rohit):
  print('Galat guess gareu mitra Ali kati badhi guess gara ')
 else:
  print('Guess lower')

 guess=int(input('Guess any number'))
 count+=1


print('correct guess')
print(count)  


#For Loop demo

for i in range(1, 11):
  print(i)