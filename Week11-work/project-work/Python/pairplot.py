class Pairplot:

    def __init__(self, df):
        self.df = df

    
    def create_pairplot(self):

        import matplotlib.pyplot as plt
        #Our figure and axes are created using the subplots() function. 
        #The subplots() function returns an instance of the figure and an array of axes objects.
        fig, ax = plt.subplots(2,2)

        #Add some padding to the subplots
        fig.tight_layout(pad=3.0) 

        #Create local variables for each species
        setosa = self.df[self.df.species == "Iris-setosa"]
        versicolor = self.df[self.df.species=='Iris-versicolor']
        virginica = self.df[self.df.species=='Iris-virginica']
        #  Create a list of colours to use for the boxplots
        colors = ['red', 'green', 'blue'] #The colours for the boxplots

        #Set the minimum and maximum values for the x and y axis for each subplot
        x1_min = self.df['sepal_length'].min() - 0.2
        x1_max = self.df['sepal_length'].max() + 0.2
        y1_min = self.df['sepal_width'].min() - 0.2
        y1_max = self.df['sepal_width'].max() + 0.2
        #Set the x and y axis limits for the first subplot
        ax[0,0].set_xlim(x1_min, x1_max)
        ax[0,0].set_ylim(y1_min, y1_max)

        #Set the minimum and maximum values for the x and y axis for each subplot
        x2_min = self.df['petal_length'].min() - 0.2
        x2_max = self.df['petal_length'].max() + 0.2
        y2_min = self.df['petal_width'].min() - 0.2
        y2_max = self.df['petal_width'].max() + 0.2
        #Set the x and y axis limits for the second subplot
        ax[0,1].set_xlim(x2_min, x2_max)
        ax[0,1].set_ylim(y2_min, y2_max)

        #Set the minimum and maximum values for the x and y axis for each subplot
        x3_min = self.df['sepal_length'].min() - 0.2
        x3_max = self.df['sepal_length'].max() + 0.2
        y3_min = self.df['petal_length'].min() - 0.2
        y3_max = self.df['petal_length'].max() + 0.2
        #Set the x and y axis limits for the third subplot
        ax[1,0].set_xlim(x3_min, x3_max)
        ax[1,0].set_ylim(y3_min, y3_max)

        #Set the minimum and maximum values for the x and y axis for each subplot
        x4_min = self.df['sepal_width'].min() - 0.2
        x4_max = self.df['sepal_width'].max() + 0.2
        y4_min = self.df['petal_width'].min() - 0.2
        y4_max = self.df['petal_width'].max() + 0.2
        #Set the x and y axis limits for the fourth subplot
        ax[1,1].set_xlim(x4_min, x4_max)
        ax[1,1].set_ylim(y4_min, y4_max)


        #Create the pairplot for the dataset
        ax[0,0].scatter(setosa["sepal_length"], setosa["sepal_width"], label="Sepal Length vs Sepal Width", facecolor="blue")
        #Create the scatter plot for sepal length vs sepal width
        ax[0,0].scatter(versicolor["sepal_length"], versicolor["sepal_width"], label="Sepal Length vs Sepal Width", facecolor="green")
        ax[0,0].scatter(virginica["sepal_length"], virginica["sepal_width"], label="Sepal Length vs Sepal Width", facecolor="red")

        ax[0,1].scatter(setosa["petal_length"], setosa["petal_width"], label="Petal Length vs Petal Width", facecolor="blue")
        #Create the scatter plot for petal length vs petal width
        ax[0,1].scatter(versicolor["petal_length"], versicolor["petal_width"], label="Petal Length vs Petal Width", facecolor="green")
        ax[0,1].scatter(virginica["petal_length"], virginica["petal_width"], label="Petal Length vs Petal Width", facecolor="red")

        ax[1,0].scatter(setosa["sepal_length"], setosa["petal_length"], label="Sepal Length vs Petal Length", facecolor="blue")
        #Create the scatter plot for sepal length vs petal length
        ax[1,0].scatter(versicolor["sepal_length"], versicolor["petal_length"], label="Sepal Length vs Petal Length", facecolor="green")
        ax[1,0].scatter(virginica["sepal_length"], virginica["petal_length"], label="Sepal Length vs Petal Length", facecolor="red")

        ax[1,1].scatter(setosa["sepal_width"], setosa["petal_width"], label="Sepal Width vs Petal Width", facecolor="blue")
        #Create the scatter plot for sepal width vs petal width
        ax[1,1].scatter(versicolor["sepal_width"], versicolor["petal_width"], label="Sepal Width vs Petal Width", facecolor="green")
        ax[1,1].scatter(virginica["sepal_width"], virginica["petal_width"], label="Sepal Width vs Petal Width", facecolor="red")

        #Set the x and y axis labels
        ax[0,0].set_xlabel("Sepal Length (cm)") #Set the x axis label for the first subplot
        ax[0,0].set_ylabel("Sepal Width (cm)") #Set the y axis label for the first subplot

        ax[0,1].set_xlabel("Petal Length (cm)") #Set the x axis label for the second subplot
        ax[0,1].set_ylabel("Petal Width (cm)") #Set the y axis label for the second subplot

        ax[1,0].set_xlabel("Sepal Length (cm)") #Set the x axis label for the third subplot
        ax[1,0].set_ylabel("Petal Length (cm)") #Set the y axis label for the third subplot

        ax[1,1].set_xlabel("Sepal Width (cm)") #Set the x axis label for the fourth subplot
        ax[1,1].set_ylabel("Petal Width (cm)") #Set the y axis label for the fourth subplot


        #Add a grid
        ax[0,0].grid() #Add a grid to the first subplot
        ax[0,1].grid() #Add a grid to the second subplot
        ax[1,0].grid() #Add a grid to the third subplot
        ax[1,1].grid() #Add a grid to the fourth subplot

        #Add a title

        ax[0,0].set_title("Sepal Length vs Sepal Width") #Add a title to the first subplot
        ax[0,1].set_title("Petal Length vs Petal Width") #Add a title to the second subplot
        ax[1,0].set_title("Sepal Length vs Petal Length") #Add a title to the third subplot
        ax[1,1].set_title("Sepal Width vs Petal Width") #Add a title to the fourth subplot

        #Save the plot as a .png file
        plt.savefig("Plots/pairplot.png")
        plt.clf() #Clear the current figure

        plt.close('all') #Close the current figure
