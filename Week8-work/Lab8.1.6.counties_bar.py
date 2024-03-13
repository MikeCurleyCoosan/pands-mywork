#Demonstrate making a bar chart  of unique occurences of values in an array
#Demonstrating more that just how to do pie plots
#Author: Michael Curley
#Date: 25/03/2019
#Taken from class notes 

#Import the numpy and matplotlib.pyplot modules
import numpy as np
import matplotlib.pyplot as plt

#Create an array of occurances
possible_counties = ['Cork', 'Kerry', 'Limerick', 'Clare', 'Tipperary', 'Waterford']
#pick 100 random counties from the array with frequencies set in p
counties = np.random.choice(possible_counties, p=[0.1, 0.3, 0.2, 0.12, 0.15, 0.13], size=(100))

#Get the unique values and their counts. This will return a tuple of two arrays
unique, counts = np.unique(counties, return_counts=True)

#Create a bar chart of the unique values
plt.bar(unique, counts) #Create a bar chart of the unique values

plt.show() #Show the plot

