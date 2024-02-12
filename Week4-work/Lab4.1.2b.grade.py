#Write a program (grade.py) that reads in a students percentagee mark and 
#prints out the corresponding grade ( the program should check that the percentage is valid)

#Modification....In practice the percentages are rounded i.e. 69.5 gets rounded to 70 so this would be a distinction.
#Modify the program in part 1 to deal with this.....

#Author: Michael Curley
import math

percentage = float(input('Enter the percentage: '))

'''#Method 1: Use of the built in round function......This works.
trueValue= round(percentage)
print(trueValue)

if percentage < 0 or percentage > 100:
    print('Please enter a number between 0 and 100')
elif trueValue < 40: #Between 0 and 39
    print('Fail')
elif trueValue < 50: #Between 40 and 49
    print('Pass')
elif trueValue < 60: #Between 50 and 59
    print('Merit 1')
elif trueValue < 70: #Between 60 and 69
    print('Merit 2')
else: #Between 70 and 100
    print('Distinction')'''

#Method 2: Get the remainder from % 1 and then use an if/else to compare if this is less than 0.5 or greater than 0.5 and round accordingly
trueValue = int(percentage) # This will round the value to the nearest integer
print(trueValue)
remainder = float(percentage % 1) #Lets us find the remainder.....which will be the fractional part input
print(remainder)

if remainder < 0.5:
    trueValue = trueValue
else:
    trueValue += 1

if percentage < 0 or percentage > 100:
    print('Please enter a number between 0 and 100')
elif trueValue < 40: #Between 0 and 39
    print('Fail')
elif trueValue < 50: #Between 40 and 49
    print('Pass')
elif trueValue < 60: #Between 50 and 59
    print('Merit 1')
elif trueValue < 70: #Between 60 and 69
    print('Merit 2')
else: #Between 70 and 100
    print('Distinction')