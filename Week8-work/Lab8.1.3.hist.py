#Write a program that plots a historgra of the salaries
#Author: Michael Curley
#Date: 13/03/2024

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
num_of_salaries = 100

np.random.seed(1)

salaries = np.random.randint(min_salary, max_salary, num_of_salaries)

plt.hist(salaries, bins=10, edgecolor="black")
plt.show()