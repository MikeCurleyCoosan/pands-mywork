import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../iris.data", names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"] ) # Read the iris dataset into a pandas dataframe

# Setting variables for comparison across the species which will be used for the subplots

#Create local variables for each species
setosa = df[df.species == "Iris-setosa"]
versicolor = df[df.species=='Iris-versicolor']
virginica = df[df.species=='Iris-virginica']

#  Create a list of colours to use for the boxplots
colors = ['red', 'green', 'blue'] #The colours for the boxplots

#Set the font for the x and y axis labels and the title 
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

fig, ax = plt.subplots(2,2)

setosa_sepal_length = setosa['sepal_length'].to_numpy()
setosa_sepal_width = setosa['sepal_width'].to_numpy()
setosa_petal_length = setosa['petal_length'].to_numpy()
setosa_petal_width = setosa['petal_width'].to_numpy()

versicolor_sepal_length = versicolor['sepal_length'].to_numpy()
versicolor_sepal_width = versicolor['sepal_width'].to_numpy()
versicolor_petal_length = versicolor['petal_length'].to_numpy()
versicolor_petal_width = versicolor['petal_width'].to_numpy()

virginica_sepal_length = virginica['sepal_length'].to_numpy()
virginica_sepal_width = virginica['sepal_width'].to_numpy()
virginica_petal_length = virginica['petal_length'].to_numpy()
virginica_petal_width = virginica['petal_width'].to_numpy()



# Plotting the 3 species to the plot 
ax[0,0].boxplot(setosa_sepal_length, positions=[2], widths=1.5, patch_artist=True, labels=['setosa'], boxprops=dict(facecolor=colors[2], color='black'))
ax[0,0].boxplot(versicolor_sepal_length, positions=[4], widths=1.5, patch_artist=True, labels=['versicolor'], boxprops=dict(facecolor=colors[1], color='black'))
ax[0,0].boxplot(virginica_sepal_length, positions=[6], widths=1.5, patch_artist=True, labels=['virginica'], boxprops=dict(facecolor=colors[0], color='black'))
#Set the x and y axis labels
ax[0,0].set_xlabel("Species") #Set the x axis label for the first subplot
ax[0,0].set_ylabel("Sepal length (cm)") #Set the y axis label for the first subplot


ax[0,1].boxplot(setosa_sepal_width, positions=[2], widths=1.5, patch_artist=True, labels=['setosa'], boxprops=dict(facecolor=colors[2], color='black'))
ax[0,1].boxplot(versicolor_sepal_width, positions=[4], widths=1.5, patch_artist=True, labels=['setosa'], boxprops=dict(facecolor=colors[1], color='black'))
ax[0,1].boxplot(virginica_sepal_width, positions=[6], widths=1.5, patch_artist=True, labels=['setosa'], boxprops=dict(facecolor=colors[0], color='black'))
#Set the x and y axis labels
ax[0,1].set_xlabel("Species") #Set the x axis label for the first subplot
ax[0,1].set_ylabel("Sepal width (cm)") #Set the y axis label for the first subplot

# Plotting the 3 species to the plot 
ax[1,0].boxplot(setosa_petal_length, positions=[2], widths=1.5, patch_artist=True, labels=['setosa'], boxprops=dict(facecolor=colors[2], color='black'))
ax[1,0].boxplot(versicolor_petal_length, positions=[4], widths=1.5, patch_artist=True, labels=['versicolor'], boxprops=dict(facecolor=colors[1], color='black'))
ax[1,0].boxplot(virginica_petal_length, positions=[6], widths=1.5, patch_artist=True, labels=['virginica'], boxprops=dict(facecolor=colors[0], color='black'))
#Set the x and y axis labels
ax[1,0].set_xlabel("Species") #Set the x axis label for the first subplot
ax[1,0].set_ylabel("Petal length (cm)") #Set the y axis label for the first subplot

# Plotting the 3 species to the plot 
ax[1,1].boxplot(setosa_petal_width, positions=[2], widths=1.5, patch_artist=True, labels=['setosa'], boxprops=dict(facecolor=colors[2], color='black'))
ax[1,1].boxplot(versicolor_petal_width, positions=[4], widths=1.5, patch_artist=True, labels=['versicolor'], boxprops=dict(facecolor=colors[1], color='black'))
ax[1,1].boxplot(virginica_petal_width, positions=[6], widths=1.5, patch_artist=True, labels=['virginica'], boxprops=dict(facecolor=colors[0], color='black'))
#Set the x and y axis labels
ax[1,1].set_xlabel("Species") #Set the x axis label for the first subplot
ax[1,1].set_ylabel("Petal width (cm)") #Set the y axis label for the first subplot


 #Add a grid
ax[0,0].grid() #Add a grid to the first subplot
ax[0,1].grid() #Add a grid to the second subplot
ax[1,0].grid() #Add a grid to the third subplot
ax[1,1].grid() #Add a grid to the fourth subplot

 #Add a title
ax[0,0].set_title("Sepal Length") #Add a title to the first subplot
ax[0,1].set_title("Sepal Width") #Add a title to the second subplot
ax[1,0].set_title("Petal Length") #Add a title to the third subplot
ax[1,1].set_title("Petal Width") #Add a title to the fourth subplot


plt.tight_layout()  # Adjust the layout of subplots to prevent overlapping
plt.savefig("../Plots/boxplot2.png")

plt.clf() # clears the current plot to allow a fresh plot for the next histogram to be created