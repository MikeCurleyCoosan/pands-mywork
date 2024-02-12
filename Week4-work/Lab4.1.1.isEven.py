#Write a program (isEven.py) that asks the user to enter a number, and the program
#will tell the user if the number is even or odd

#Modify the program to use a while loop so the program keeps prompting the user for
#more numbers until the user enters -1

#Author: Michael Curley

number = int(input("Please enter an integer: "))


while number != -1:
    if (number % 2) == 0:
        print(f'{number} is an even number')
        number = int(input('Please enter a integer: '))
    else:
        print(f'{number} is an odd number')
        number = int(input('Please enter an integer: '))