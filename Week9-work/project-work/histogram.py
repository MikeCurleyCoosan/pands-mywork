#Import the required libraries
import matplotlib.pyplot as plt

#Final version of the code to create a histogram for each variable for each species on the same plot
#Create a function to create histograms for each variable
def create_histogram(df, variable): #The function takes in two parameters, the dataframe and the variable to create the histogram foran
    #Using the dataframe we can create local variable for each species, therefore we can amalgamate each species onto our histogram in different colours
    setosa = df[df.species == "Iris-setosa"]
    versicolor = df[df.species=='Iris-versicolor']
    virginica = df[df.species=='Iris-virginica']

    #The stateless approach to creating a histogram as recommended by real python website
    #https://realpython.com/python-matplotlib-guide/
    #https://realpython.com/python-histograms/ 
    fig, ax = plt.subplots()

    #Create the histogram for the same variable for each species on the one plot. Therefore three histograms will be 
    #created on the same plot.
    ax.hist(setosa[variable], bins=10, label="Setosa", color="blue", alpha=0.5, edgecolor='black') #The alpha parameter is used to make the bars transparent
    ax.hist(versicolor[variable], bins=10, label="Versicolor", color="green", alpha=0.5, edgecolor='black')
    ax.hist(virginica[variable], bins=10, label="Virginica", color="red", alpha=0.5, edgecolor='black')

    #Set the font for the x and y axis labels and the title (https://www.w3schools.com/python/matplotlib_labels.asp)
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    #Set the x and y axis labels
    ax.set_xlabel(variable.capitalize().replace('_', ' '), fontdict=font2)
    ax.set_ylabel("Frequency", fontdict=font2)
    
    #Add a title
    ax.set_title(variable.capitalize().replace('_', ' '), fontdict=font1)

    #Add a grid
    ax.grid(linestyle='--', linewidth=0.5, color='black', alpha=0.4)

    #Add a legend
    ax.legend()

    #Save the plot as a .png file
    plt.savefig("Plots/" + variable + "_histogram.png")
    plt.clf()