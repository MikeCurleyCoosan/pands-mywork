class GetVariables:
    def __init__(self, df):
        self.df = df

    def get_variables(self):
        import numpy as np
        #Get the variables in the dataset
        variables = self.df.columns.to_numpy()
        variables = np.delete(variables, 4) #Remove the species variable from the list of variables
        return variables

