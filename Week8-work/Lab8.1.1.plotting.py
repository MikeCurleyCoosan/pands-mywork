#Write a program that makes a list, called salaries, and that has 10 random numbers (20000 <= number <= 80000) and then plot them

#Author: Michael Curley
#Date: 13/03/2024

import numpy as np



min_salary = 20000
max_salary = 80000
num_of_salaries = 10

#This is so that the random numbers generated are the same each time the program is run. This will make it easier to debug the program
np.random.seed(1)

salaries = np.random.randint(min_salary, max_salary, num_of_salaries)

print(salaries)

#Add 500 to each salary in the numpy array. This is called broadcasting. We cannot do this with a list in python. We would have to use a loop.
salaries_plus = salaries + 5000 #Add 5000 to each salary
print(salaries_plus)

#you can also multiply, divide, subtract, and use the power of operator on numpy arrays
salaries_mult = salaries * 1.05 #Add 5% to each salary
print(salaries_mult)

#This is a floating point array, as we are multiplying by a floating point number. Convert to an integer array
new_salaries = salaries_mult.astype(int)
print(new_salaries)


