class Menu:
#Author: Michael Curley
#This class is used to display a menu to the user and run the code based on the user's choice

    #Import the pandas library
    import pandas as pd
    #Constructor
    def __init__(self):
        pass

    #Read in the iris dataset and store it in the variable df
    df = pd.read_csv('iris.data', names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

    #display_menu function, which displays a menu to the user
    def display_menu():
        print("What would you like to do?") # Print the menu
        print("\t(a) create a summary.txt file")  #create a summary.txt file
        print("\t(b) create histograms of variables")    #create histograms of variables
        print("\t(c) create scatter plots of pairs of variables")    #create scatter plots of pairs of variables
        print("\t(d) create a boxplot of variables")    #create a pairplot of the dataset
        print("\t(e) create a pairplot of the dataset")    #create a pairplot of the dataset
        print("\t(f) create a correlation matrix/heatmap for the dataset")    #create a correlation matrix for the dataset
        print("\t(g) Run all code and create summary.txt, correlation.txt, all .png files, and correlation heat map")  #Run all code and create summary.txt, correlation.txt, all .png files, and correlation heat map
        print("\t(h) Create best fit line for scatter plots")  #Create best fit line for scatter plots
        print("\t(q) Quit")  #Quit
        choice = input("Type one letter (a/b/c/d/e/f/g/h/q):").strip()

        return choice

    #do_summary function which takes in a dataframe and creates a summary.txt file
    def do_summary(df, FILENAME="summary.txt"):
        print("Creating summary.txt file")
        #Import the Summary class from the summary.py file
        from Python.summary import Summary as sm
        #Create an instance of the Summary class
        summary = sm()
        #Call the create_summary method of the Summary class and pass in the dataframe and the name of the file to write the summary to
        summary.create_summary(df, FILENAME) #Create a summary.txt file
        #Print a message to the user
        print("Summary.txt file created")

    #do_histogram function which takes in a dataframe and creates histograms of variables
    def do_histogram(df):
        print("Creating histograms of variables")
        #Import the Histogram class from the histogram.py file
        from Python.histogram import Histogram as hist
        #Import the GetVariables class from the get_variables.py file
        from Python.get_variables import GetVariables as gv
        #Create an instance of the GetVariables class
        get_variables = gv(df)
        #Call the get_variables method of the GetVariables class
        my_var = get_variables.get_variables()
        #Create an instance of the Histogram class
        histogram = hist()
        #For each variable in the dataset
        for variable in my_var: #For each variable in the dataset
            histogram.create_histogram(df, variable) #Create a histogram of the variable and save it as a .png file
        #Print a message to the user
        print("Histograms created")

    #do_scatter_plot function which takes in a dataframe and creates scatter plots of pairs of variables
    def do_scatter_plot(df):
        print("Creating scatter plots of pairs of variables")
        from Python.scatterplot import Scatterplot as sp
        from Python.get_variables import GetVariables as gv
        get_variables = gv(df)
        my_var = get_variables.get_variables()
        scatterplot = sp(df)
        for i in range(len(my_var)): #For each pair of variables in the dataset
            for j in range(i+1, len(my_var)): 
                scatterplot.create_scatter_plot(my_var[j], my_var[i]) #Create a scatter plot of the two variables and save it as a .png file
        print("Scatter plots created")

    #do_boxplot function which takes in a dataframe and creates a boxplot of variables
    def do_boxplot(df):
        print("Creating a boxplot of variables")
        #Import the Boxplot class from the boxplot.py file
        from Python.boxplot import Boxplot as box
        #Import the GetVariables class from the get_variables.py file
        from Python.get_variables import GetVariables as gv
        #Create an instance of the GetVariables class
        get_variables = gv(df)
        #Call the get_variables method of the GetVariables class
        my_var = get_variables.get_variables()
        #Create an instance of the Boxplot class
        boxplot = box()
        #For each variable in the dataset
        for variable in my_var: #For each variable in the dataset
            boxplot.create_boxplot(df, variable) #Create a boxplot of the variable and save it as a .png file
        print("Boxplot created")

    #do_pairplot function which takes in a dataframe and creates a pairplot of the dataset
    def do_pairplot(df):
        print("Creating a pairplot of the dataset")
        #Import the Pairplot class from the pairplot.py file
        from Python.pairplot import Pairplot as pp
        #Create an instance of the Pairplot class
        pairplot = pp(df)
        #Call the create_pairplot method of the Pairplot class
        pairplot.create_pairplot() #Create a pairplot of the dataset and save it as a .png file
        print("Pairplot created")

    #do_correlation_matrix function which takes in a dataframe and creates a correlation matrix for the dataset
    def do_correlation_matrix(df):
        print("Creating a correlation matrix/heatmap for the dataset")
        #Import the Correlation class from the correlation.py file
        from Python.correlation import Correlation as corr
        #Create an instance of the Correlation class
        correlation = corr()
        #Call the create_correlation_matrix method of the Correlation class
        correlation.create_correlation_matrix(df) #Create a correlation matrix for the dataset. This also creates a heatmap of the correlation matrix
        print("Correlation matrix/heatmap created")

    #do_best_fit function which takes in a dataframe and creates a best fit line for the petal length and petal width variables
    def do_best_fit(df):
        print("Creating best fit line for scatter plots")
        #Import the BestFit class from the best_fit.py file
        from Python.best_fit import BestFit as bf
        #Create an instance of the BestFit class
        best_fit = bf(df)
        #Call the best_fit method of the BestFit class
        best_fit.best_fit()
        #Print a message to the user
        print("Best fit line created")

    #do_all_code function which takes in a dataframe and runs all code and creates summary.txt, correlation.txt, all .png files, and correlation heat map
    def do_all_code(df, FILENAME="summary.txt"):
        print("Running all code and creating summary.txt, correlation.txt, all .png files, and correlation heat map")
        #Import the required classes from the Python folder
        from Python.correlation import Correlation as corr
        from Python.pairplot import Pairplot as pp
        from Python.histogram import Histogram as hist
        from Python.boxplot import Boxplot as box
        from Python.scatterplot import Scatterplot as sp
        from Python.best_fit import BestFit as bf
        from Python.summary import Summary as sm
        from Python.get_variables import GetVariables as gv
        #Create an instance of the GetVariables class
        get_variables = gv(df)
        #Call the get_variables method of the GetVariables class
        my_var = get_variables.get_variables()
        #Create instances of the required classes
        summary = sm()
        histogram = hist()
        boxplot = box()
        scatterplot = sp(df)
        pairplot = pp(df)
        correlation = corr()
        #Call the required methods of the classes
        summary.create_summary(df, FILENAME)
        #For each variable in the dataset
        for variable in my_var:
            #Create a histogram of the variable and save it as a .png file
            histogram.create_histogram(df, variable)
            #Create a boxplot of the variable and save it as a .png file
            boxplot.create_boxplot(df, variable)
        #For each pair of variables in the dataset
        for i in range(len(my_var)):
            for j in range(i+1, len(my_var)):
                #Create a scatter plot of the two variables and save it as a .png file
                scatterplot.create_scatter_plot(my_var[j], my_var[i])
        #Create a pairplot of the dataset and save it as a .png file        
        pairplot.create_pairplot()
        #Create a correlation matrix for the dataset. This also creates a heatmap of the correlation matrix
        correlation.create_correlation_matrix(df)
        print("All code run and files created")


    #do_nothing function which takes in a dummy parameter and does nothing
    def do_nothing(dummy):
        pass

    #the choice_map dictionary which maps a letter to a function
    choice_map = {
        "a": do_summary,
        "b": do_histogram,
        "c": do_scatter_plot, 
        "d": do_boxplot,
        "e": do_pairplot,
        "f": do_correlation_matrix,
        "g": do_all_code,
        "h": do_best_fit,
        "q": do_nothing
    }
