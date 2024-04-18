class Menu:
    #Constructor
    def __init__(self):
        pass

    #Importing the necessary libraries
    import pandas as pd
    
    from Python.correlation import Correlation as corr
    from Python.pairplot import Pairplot as pp
    from Python.histogram import Histogram as hist
    from Python.boxplot import Boxplot as box
    from Python.scatterplot import Scatterplot as sp
    from Python.get_variables import GetVariables as gv
    from Python.best_fit import BestFit as bf

    #Read in the iris dataset and store it in the variable df
    df = pd.read_csv('iris.data', names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])
    #Create a variable to store the name of the summary file
    FILENAME = "summary.txt"
    #Create a list of the variables in the dataset
    get_variables = gv(df)
    my_var = get_variables.get_variables()

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
    def do_summary(df):
        print("Creating summary.txt file")
        from Python.summary import Summary as sm
        summary = sm()
        summary.create_summary(df, FILENAME) #Create a summary.txt file
        print("Summary.txt file created")

    #do_histogram function which takes in a dataframe and creates histograms of variables
    def do_histogram(df):
        print("Creating histograms of variables")
        from Python.histogram import Histogram as hist
        from Python.get_variables import GetVariables as gv
        get_variables = gv(df)
        my_var = get_variables.get_variables()
        histogram = hist()
        for variable in my_var: #For each variable in the dataset
            histogram.create_histogram(df, variable) #Create a histogram of the variable and save it as a .png file
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
        from Python.boxplot import Boxplot as box
        from Python.get_variables import GetVariables as gv
        boxplot = box()
        for variable in my_var: #For each variable in the dataset
            boxplot.create_boxplot(df, variable) #Create a boxplot of the variable and save it as a .png file
        print("Boxplot created")

    #do_pairplot function which takes in a dataframe and creates a pairplot of the dataset
    def do_pairplot(df):
        print("Creating a pairplot of the dataset")
        import Python.pairplot as pp
        pairplot = pp(df)
        pairplot.create_pairplot() #Create a pairplot of the dataset and save it as a .png file
        print("Pairplot created")

    #do_correlation_matrix function which takes in a dataframe and creates a correlation matrix for the dataset
    def do_correlation_matrix(df):
        print("Creating a correlation matrix/heatmap for the dataset")
        import Python.correlation as corr
        correlation = corr()
        correlation.create_correlation_matrix(df) #Create a correlation matrix for the dataset. This also creates a heatmap of the correlation matrix
        print("Correlation matrix/heatmap created")

    def do_best_fit(df):
        print("Creating best fit line for scatter plots")
        import Python.best_fit as bf
        best_fit = bf(df)
        best_fit.best_fit()
        print("Best fit line created")

    #do_all_code function which takes in a dataframe and runs all code and creates summary.txt, correlation.txt, all .png files, and correlation heat map
    def do_all_code(df):
        print("Running all code and creating summary.txt, correlation.txt, all .png files, and correlation heat map")
        import Python.summary as sm
        import Python.histogram as hist
        import Python.boxplot as box
        import Python.scatterplot as sp
        import Python.pairplot as pp
        import Python.correlation as corr

        summary = sm()
        histogram = hist()
        boxplot = box()
        scatterplot = sp(df)
        pairplot = pp(df)
        correlation = corr()
        summary.create_summary(df, FILENAME)
        for variable in my_var:
            histogram.create_histogram(df, variable)
            boxplot.create_boxplot(df, variable)
        for i in range(len(my_var)):
            for j in range(i+1, len(my_var)):
                scatterplot.create_scatter_plot(my_var[j], my_var[i])
        pairplot.create_pairplot(df)
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
