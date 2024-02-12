#Write a program (average.py) that keeps reading numbers until the user enters a 0.
#The program should append each of them onto a list. The program should then print out each of the
#numbers entered and the average of them.

#Author: Michael Curley

numbers = [] #Create an empty list to store numbers

number = int(input('Enter a number (0 to quit): '))

while number !=0:
    numbers.append(number)

    number = int(input('Enter another number (0 to quit): '))

for value in numbers:
    print(value)

average = float(sum(numbers) / len(numbers))
print ('The average is {}'.format(average))