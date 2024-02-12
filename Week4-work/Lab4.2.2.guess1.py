#Write a program (guess1.py) that prompts teh user to guess a number, the program
#should keep prompting the user to guess the number until the user gets the right one.

numToGuess = 30

guess = int(input('Please guess the number: '))

while guess != numToGuess:
    print('Sorry, wrong answer')
    guess = int(input("Please guess again: "))

print("Well done, yes the number was {}".format(numToGuess))