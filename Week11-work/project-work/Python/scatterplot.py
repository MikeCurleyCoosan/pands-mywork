class Scatterplot:
    def __init__(self, df):
        self.df = df

    #Use same approach as above to create a scatter plot for each pair of variables. Therefore we create a function to create the scatter plots
    def create_scatter_plot(self, x, y): #The function takes in three parameters, the dataframe and the two variables to create the scatter plot for
        # Import the required libraries
        import matplotlib.pyplot as plt

        #Create local variables for each species
        setosa = self.df[self.df.species == "Iris-setosa"]
        versicolor = self.df[self.df.species=='Iris-versicolor']
        virginica = self.df[self.df.species=='Iris-virginica']

        #Our figure and axes are created using the subplots() function. 
        #The subplots() function returns an instance of the figure and an array of axes objects.
        fig, ax = plt.subplots()

        #Create the scatter plot for the two variables for each species on the one plot. Therefore three scatter plots will be
        #created on the same plot.
        ax.scatter(setosa[x], setosa[y], label="Setosa", facecolor="blue")
        ax.scatter(versicolor[x], versicolor[y], label="Versicolor", facecolor="green")
        ax.scatter(virginica[x], virginica[y], label="Virginica", facecolor="red")

        #Set the font for the x and y axis labels and the title (https://www.w3schools.com/python/matplotlib_labels.asp)
        font1 = {'family':'serif','color':'blue','size':20}
        font2 = {'family':'serif','color':'darkred','size':15}

        #Set the x and y axis labels
        ax.set_xlabel(x.capitalize().replace('_', ' ')+ " (cm)", fontdict=font2)
        ax.set_ylabel(y.capitalize().replace('_', ' ') + " (cm)", fontdict=font2)

        #Add a grid
        ax.grid(linestyle='--', linewidth=0.5, color='black', alpha=0.4)

        #Add a title
        ax.set_title("Iris " + x.capitalize().replace('_', ' ') + " vs " + y.capitalize().replace('_', ' '), fontdict=font1)

        #Add a legend
        ax.legend()

        #Save the plot as a .png file
        plt.savefig("Plots/" + x + "_vs_" + y + "_scatter.png")
        plt.clf() #Clear the current figure
        plt.close('all') #Close the current figure



































