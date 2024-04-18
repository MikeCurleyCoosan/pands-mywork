class GetVariables:
#Author: Michael Curley
#This class is used to get the variables from a dataset

    #Constructor. This is the code that is run when a new instance of the class is created. Here we pass in the dataframe
    def __init__(self, df):
        self.df = df

    #Create a function to get the variables in the dataset
    def get_variables(self):
        #Import the required libraries 
        import numpy as np
        #Get the variables in the dataset
        variables = self.df.columns.to_numpy() #Convert the columns of the dataframe to a numpy array to get the variables
        variables = np.delete(variables, 4) #Remove the species variable from the list of variables, as it is not needed
        return variables #Return the variables

