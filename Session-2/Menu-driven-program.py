#Menu Driven Calculation

fnum = int(input('Enter the first number\n'))
snum = int(input('Enter the second number\n'))

op = input('Enter the operation\n')

if op== '+':
    print(fnum + snum)

elif op == '-':
    print(fnum - snum)

elif op == '*':
    print(fnum * snum)

else :
    print (fnum / snum)


#Lets do another program

menu = input("""
Hi! How can I help you
1. Enter 1 for pin change
2. Enter 2 for balance check
3. Enter 3 for Withdrawal
4. Enter 4 for Exit

""")

if menu == '1':
    print('Pin changed')

elif menu == '2':
    print('Balance Checked')

elif menu == '3':
    print('Withdrawal done')

else :
    print('Exit')