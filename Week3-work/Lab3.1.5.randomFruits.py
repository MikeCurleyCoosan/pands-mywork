#This program prints out a random fruit
#Author: Michael Curley (with help of PANDS class notes)

import random

#List of fruits in python
fruits = ['Apple', 'Orange', 'Banana', 'Pear']

#We want a random number which is between zero and the length of the list
index = random.randint(0,len(fruits)-1)

#pick the fruit from the list at index and assign it to variable randomFruit
randomFruit = fruits[index]

#Print your answer
print("A Random Fruit is a {}".format(randomFruit))