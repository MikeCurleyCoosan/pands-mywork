# Import the required libraries
import matplotlib.pyplot as plt

#Create a function to create a boxplot for each variable
def create_boxplot(df, variable): #The function takes in two parameters, the dataframe and the variable to create a boxplot for.

    #Create local variables for each species
    setosa = df[df.species == "Iris-setosa"]
    versicolor = df[df.species=='Iris-versicolor']
    virginica = df[df.species=='Iris-virginica']

    #Create a list of colours to use for the boxplots
    colors = ['red', 'green', 'blue'] #The colours for the boxplots

    #Our figure and axes are created using the subplots() function. 
    #The subplots() function returns an instance of the figure and an array of axes objects.
    fig, ax = plt.subplots()

    #Create a boxplot for each variable on one plot. Therefore three boxplots will be created on the same plot.
    ax.boxplot(setosa[variable], positions=[2], widths=1.5, patch_artist=True, labels=['setosa'], boxprops=dict(facecolor=colors[2], color='black'))
    #positions=[2] is used to position the boxplot on the x-axis
    #widths=1.5 is used to set the width of the boxplot
    #patch_artist=True is used to fill the boxplot with colour
    #labels=['setosa'] is used to label the boxplot
    #boxprops=dict(facecolor=colors[2], color='black') is used to set the colour of the boxplot

    #We have created a boxplot for setosa and now we need to create a boxplot for versicolor and virginica
    ax.boxplot(versicolor[variable], positions=[4], widths=1.5, patch_artist=True, labels=['versicolor'], boxprops=dict(facecolor=colors[1], color='black'))
    ax.boxplot(virginica[variable], positions=[6], widths=1.5, patch_artist=True, labels=['virginica'], boxprops=dict(facecolor=colors[0], color='black'))

    #Set the font for the x and y axis labels and the title 
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    #Add a title to the boxplot
    fig.suptitle("Boxplot of " + variable.capitalize().replace('_', ' '), fontdict=font1)

    #Variables to set the minimum and maximum values for the y-axis
    min = df[variable].min() - 0.2
    max = df[variable].max() + 0.2

    #Set the y-axis limits
    ax.set_ylim(min, max)

    #Add some padding to the subplots
    fig.tight_layout(pad=3.0) 

    #Set the x and y axis labels
    ax.set_xlabel("Species", fontdict=font2)
    ax.set_ylabel(variable.capitalize().replace('_', ' ') + " (cm)", fontdict=font2)

    #Add a grid
    ax.grid(linestyle='--', linewidth=0.5, color='black', alpha=0.4)


    #Save the plot as a .png file
    plt.savefig("Plots/" + variable + "_boxplot.png")
    plt.clf() #Clear the current figure