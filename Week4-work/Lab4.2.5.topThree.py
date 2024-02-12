#Write a program (topThree.py) which generates 10 random numbers (0-100), prints them out
#and then prints out the top three.

#Author: Michael Curley

import random

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers =[]

for i in range (0,howMany):
    numbers.append(random.randint(rangeFrom,rangeTo))

print('{} random numbers \t {}'.format(howMany, numbers))

topOnes = numbers.copy()

topOnes.sort(reverse = True)
print('The top {} are \t\t {}'.format(topHowMany, topOnes[0:topHowMany]))