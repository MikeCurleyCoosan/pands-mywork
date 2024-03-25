#Import the necessary libraries
import numpy as np

#Create a function to get the variables in the dataset   
def get_variables(df):
    #Get the variables in the dataset
    variables = df.columns.to_numpy()
    variables = np.delete(variables, 4) #Remove the species variable from the list of variables
    return variables
