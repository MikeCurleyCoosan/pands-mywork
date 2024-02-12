#Write a program (guess1.py) that prompts teh user to guess a number, the program
#should keep prompting the user to guess the number until the user gets the right one.

#Modification.....How would you modify the program, so that the program tells the user
#if there guess is too high or too low, each time they guess. HINT: put an if statement inside the while loop

#Extra.....Get the program to generate a random number between 0 and 100 to guess

import random

numToGuess = random.randint(0,100)

guess = int(input('Please guess the number: '))

while guess != numToGuess:
    if guess < numToGuess:
        print('Sorry, wrong answer, your guess is too low')
    else: 
        print('Sorry, wrong answer, your guess is too high')
    guess = int(input("Please guess again: "))

print("Well done, yes the number was {}".format(numToGuess))