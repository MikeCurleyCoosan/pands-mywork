class Analysis:
    # This is my analysis of the iris dataset for the programming and scripting module project in ATU 2024.
    # THis is the main program which calls the display_menu function from the menu.py file and then calls the appropriate function based on the user's choice

    # Author: Michael Curley\
    from Python.menu import Menu as m
    import pandas as pd

    #Read in the iris dataset and store it in the variable df
    df = pd.read_csv('iris.data', names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]) #Read in the iris dataset and store it in the variable df

    #Main program
    choice = m.display_menu() #Call the display_menu function and store the result in the variable choice
    while choice != "q": #While the user's choice is not q
        if choice in m.choice_map: #If the user's choice is in the choice_map dictionary
            m.choice_map[choice](df) 
        else:
            print("Please select either a,v or q") #If the user's choice is not in the choice_map dictionary, print an error message
        choice = m.display_menu()
