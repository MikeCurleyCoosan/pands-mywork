class Summary:

    # Create a function to display a summary of the dataset into a file called summary.txt
    def create_summary(self, df, FILENAME): #The function takes in two parameters, the dataframe and the name of the file to write the summary to.
        FILENAME = "summary.txt"
    
        #Create a file called summary.text and have the file ready to write to. If the file already exists it will be overwritten.
        with open('summary.txt', 'w') as file:
        
            #Write the first line to the file
            file.write("Summary of the Iris Dataset\n")
            file.write("\n") #Add a new line to the file
            
            
            file.write("****************************************************************************************************\n")
    
            # Write a summary of the dataset to the file
            file.write('\n')
            file.write("Summary of the dataset\n\n")
            #The describe() function applies basic statistical computations on the dataset like extreme values, 
            #count of data points standard deviation, etc. Any missing value or NaN value is automatically skipped. 
            #describe() function gives a good picture of the distribution of data
            #https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
            file.write(df.describe().to_string() + "\n")  #The summary of the dataset
            file.write("\n")
    
    
            file.write("****************************************************************************************************\n")
    
            # Write a summary of the Sepal Length variable to the file
            file.write('\n')
            file.write("Summary of the Sepal Length Variable of the Dataset\n\n")
            #The describe() function applies basic statistical computations on the dataset like extreme values, 
            #count of data points standard deviation, etc. Any missing value or NaN value is automatically skipped. 
            #describe() function gives a good picture of the distribution of data
            #https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
            sepal_length_summary = df[["sepal_length", "species"]].groupby("species").describe()
            file.write(sepal_length_summary.to_string() + "\n\n")
            file.write("\n")
            file.write("****************************************************************************************************\n")
    
            # Write a summary of the Sepal Width variable to the file
            file.write('\n')
            file.write("Summary of the Sepal Width Variable of the Dataset\n\n")
            #The describe() function applies basic statistical computations on the dataset like extreme values, 
            #count of data points standard deviation, etc. Any missing value or NaN value is automatically skipped. 
            #describe() function gives a good picture of the distribution of data
            #https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
            sepal_width_summary = df[["sepal_width", "species"]].groupby("species").describe()
            file.write(sepal_width_summary.to_string() + "\n\n")
            file.write("\n")
            file.write("****************************************************************************************************\n")
    
            # Write a summary of the Petal Length variable to the file
            file.write('\n')
            file.write("Summary of the Petal Length Variable of the Dataset\n\n")
            #The describe() function applies basic statistical computations on the dataset like extreme values, 
            #count of data points standard deviation, etc. Any missing value or NaN value is automatically skipped. 
            #describe() function gives a good picture of the distribution of data
            #https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
            petal_length_summary = df[["petal_length", "species"]].groupby("species").describe()
            file.write(petal_length_summary.to_string() + "\n\n")
            file.write("\n")
            file.write("****************************************************************************************************\n")
    
            # Write a summary of the Petal Width to the file
            file.write('\n')
            file.write("Summary of the Petal Width Variable of the Dataset\n\n")
            #The describe() function applies basic statistical computations on the dataset like extreme values, 
            #count of data points standard deviation, etc. Any missing value or NaN value is automatically skipped. 
            #describe() function gives a good picture of the distribution of data
            #https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
            petal_width_summary = df[["petal_width", "species"]].groupby("species").describe()
            file.write(petal_width_summary.to_string() + "\n\n")
            file.write("\n")
            file.write("****************************************************************************************************\n")
    
            #Write the number of rows and columns in the dataset to the file
            file.write('\n')
            file.write("Number of rows and columns in the dataset\n\n")
            rows_columns = df.shape #The number of rows and columns in the dataset
            file.write("Number of rows: " + str(rows_columns[0]) + "\n")  #The number of rows in the dataset
            file.write("Number of columns: " + str(rows_columns[1]) + "\n")  #The number of columns in the dataset
            file.write("\n")
    
            file.write("****************************************************************************************************\n")
        
            #Write the number of missing values in the dataset to the file
            file.write('\n')
            file.write("Number of missing values in the dataset\n\n")
            file.write(df.isnull().sum().to_string() + "\n")  #The number of missing values in the dataset
            file.write("\n")
    
    
            file.write("****************************************************************************************************\n")
    
            #Write the number of duplicates in the dataset to the file
            file.write('\n')
            file.write("Number of duplicates in the dataset\n")
            file.write(str(df.duplicated().sum()) + "\n")  #The number of duplicates in the dataset
            file.write("\n")
    
            file.write("****************************************************************************************************\n")
    
            #Write the number of unique values in the dataset to the file
            file.write('\n')
            file.write("Number of unique values in the dataset\n")
            file.write(df.nunique().to_string() + "\n")  #The number of unique values in the dataset
            file.write("\n")
    
            file.write("****************************************************************************************************\n")
    
            #Checking the group size of each species
            file.write('\n')
            file.write("Group size of each species\n")
            file.write(df.groupby('species').size().to_string() + "\n")  #The group size of each species
            file.write("\n")
    
            file.write("****************************************************************************************************\n")