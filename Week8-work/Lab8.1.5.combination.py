#Have two differnt plots in the same figure
#Author: Michael Curley
#Date: 25/03/2019

#Import the numpy and matplotlib.pyplot modules
import numpy as np
import matplotlib.pyplot as plt

#Create our variables
low_salary = 20000
high_salary = 80000
number_of_salaries = 100

#Create a list of random salaries
salaries = np.random.randint(low_salary, high_salary, number_of_salaries)

#Create a list of random ages
ages = np.random.randint(low=21, high=65, size = number_of_salaries) #Not a good idea, better to have absolute values for low and high created as variables

#Create a scatter plot of the data
plt.scatter(ages, salaries, color='b', label = "Salaries") #Create a scatter plot of the data. This will be random
plt.xlabel("Ages") #Label the x-axis
plt.ylabel("Salaries") #Label the y-axis
plt.title("Random Salaries and Ages") #Title the plot
plt.legend() #Show the legend

#Add x_squared
x_points = np.array(range(1,101))
y_points = x_points * x_points

plt.plot(x_points, y_points, color='r', label = "x^2") #Create a scatter plot of the data. This will be random  

plt.title("Random Salaries and Ages") #Title the plot

plt.savefig('prettier_plot.png') #Save the plot to a file

#plt.show() #Show the plot