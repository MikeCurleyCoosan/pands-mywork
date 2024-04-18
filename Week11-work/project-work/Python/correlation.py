class Correlation:
#Author: Michael Curley
#This class is used to create a correlation matrix for a dataset

    #Constructor. This is the code that is run when a new instance of the class is created.
    def __init__(self):
        pass

    #Create a function to create a correlation matrix for the dataset
    def create_correlation_matrix(self, df):

        #Import the required libraries
        import matplotlib.pyplot as plt
        import seaborn as sns

        #Create a correlation matrix for the dataset
        df_corr = df.drop(columns='species') # Drop the species column as it is not needed for the correlation matrix

        #Create a correlation matrix of the dataset
        CORRELATION = df_corr.corr()
        #The corr() function is used to calculate the correlation between each variable in the dataset

        
        #We will save the correlation matrix to a file called correlations.txt
        with open("Correlation/correlations.txt", 'w') as f:

            #Write the correlation matrix to the file
            f.write("Correlation Matrix of the Iris Dataset\n")
            f.write("\n") #Add a new line to the file
            f.write("****************************************************************************************************\n")
            f.write("\n")
            f.write(CORRELATION.to_string() + "\n\n")  #The correlation matrix of the dataset
            f.write("\n")
            f.write("****************************************************************************************************\n")
            f.write("\n")
            f.write("The correlation matrix shows the correlation between each variable in the dataset.\n")
            f.write("The correlation coefficient ranges from -1 to 1. If the value is close to 1,\n")
            f.write("it means that there is a strong positive correlation between the two variables.\n")
            f.write("If the value is close to -1, it means that there is a strong negative correlation between the two variables.\n")
            f.write("If the value is close to 0, it means that there is no correlation between the two variables.\n")

        #Create a heatmap of the correlation matrix
        fig, ax = plt.subplots() # Create a figure and axis

        corr_map = sns.heatmap(CORRELATION, annot=True, cmap='coolwarm') # Create a heatmap of the correlation matrix
        #cmap is used to set the colour map for the heatmap
        # fixed an initial issue where axis labels were being cut off: 
        #https://stackoverflow.com/questions/33660420/seaborn-ticklabels-are-being-truncated 
        plt.savefig('Correlation/correlation_heatmap.png') # Save the heatmap as a .png file
        plt.clf()

        plt.close('all') # Close the current figure