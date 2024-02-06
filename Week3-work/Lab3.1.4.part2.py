#Program that prints out a random number between 1 and 10
#Author: Michael Curley

import random

a = int(input("Please input the lower range number: "))
b = int(input("Please input the upper ranger number: "))

number = random.randint(a,b)

print("here is a random number {}".format(number))