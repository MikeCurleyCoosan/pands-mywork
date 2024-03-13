# Write a program that plots the function y = x^2
# Author: Michael Curley
# Date: 13/03/2024

import numpy as np
import matplotlib.pyplot as plt

x_points = np.array(range(1,101))   # Create an array of x values from 1 to 100
y_points = x_points * x_points      # Create an array of y values which are the square of the x values

plt.plot(x_points, y_points)        # Plot the x and y values
plt.show()                          # Show the plot