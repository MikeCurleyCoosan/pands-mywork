#Write a program (grade.py) that reads in a students percentagee mark and 
#prints out the corresponding grade ( the program should check that the percentage is valid)

#Author: Michael Curley

percentage = float(input('Enter the percentage: '))

if percentage < 0 or percentage > 100:
    print('Please enter a number between 0 and 100')
elif percentage < 40: #Between 0 and 39
    print('Fail')
elif percentage < 50: #Between 40 and 49
    print('Pass')
elif percentage < 60: #Between 50 and 59
    print('Merit 1')
elif percentage < 70: #Between 60 and 69
    print('Merit 2')
else: #Between 70 and 100
    print('Distinction')