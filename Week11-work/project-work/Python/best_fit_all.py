class BestFitAll:

    def __init__(self, df):
        self.df = df


    # Define the function that will be called from the main program
    def bestfit_all(iris):

        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns

        # Extract the petal lengths as NumPy arrays (for polyfit)
        setosa_plen = df.loc[df['species']=="setosa", 'petal_length'].to_numpy()
        versicolor_plen = df.loc[df['species']=="versicolor", 'petal_length'].to_numpy()
        virginica_plen = df.loc[df['species']=="virginica", 'petal_length'].to_numpy()
        iris_plen = df['petal_length'].to_numpy()

        # Extract the petal widths as NumPy arrays (for polyfit)
        setosa_pwth = df.loc[df['species']=="setosa", 'petal_width'].to_numpy()
        versicolor_pwth = df.loc[df['species']=="versicolor", 'petal_width'].to_numpy()
        virginica_pwth = df.loc[df['species']=="virginica", 'petal_width'].to_numpy()
        iris_pwth = df['petal_width'].to_numpy()

        # Extract the sepal lengths as NumPy arrays (for polyfit)
        setosa_slen = df.loc[df['species']=="setosa", 'sepal_length'].to_numpy()
        versicolor_slen = df.loc[df['species']=="versicolor", 'sepal_length'].to_numpy()
        virginica_slen = df.loc[df['species']=="virginica", 'sepal_length'].to_numpy()
        iris_slen = df['sepal_length'].to_numpy()

        # Extract the sepal widths as NumPy arrays (for polyfit)
        setosa_swth = df.loc[df['species']=="setosa", 'sepal_width'].to_numpy()
        versicolor_swth = df.loc[df['species']=="versicolor", 'sepal_width'].to_numpy()
        virginica_swth = df.loc[df['species']=="virginica", 'sepal_width'].to_numpy()
        iris_swth = df['sepal_width'].to_numpy()

        # Create a figure with 6 Axes (subplots), as the number of pairwise scatterplots for 4 variables
        # will be (4 x 3)/2 = 6 in total
        fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12,9), sharex='col')

        plots = {'ax1':axes[0,0], 'ax2':axes[0,1], 'ax3':axes[0,2], 'ax4':axes[1,0], 'ax5':axes[1,1], 'ax6':axes[1,2]}
        setosa_arrays = [setosa_plen, setosa_pwth, setosa_slen, setosa_swth]
        versicolor_arrays = [versicolor_plen, versicolor_pwth, versicolor_slen, versicolor_swth]
        virginica_arrays = [virginica_plen, virginica_pwth, virginica_slen, virginica_swth]
        iris_arrays = [iris_plen, iris_pwth, iris_slen, iris_swth]

        for i in range(3):
            for key, value in plots.items():

                value.scatter(setosa_arrays[i], setosa_arrays[i+1], label="setosa", color='red', edgecolor='black')  
                value.scatter(versicolor_arrays[i], versicolor_arrays[i+1], label="versicolor", color='blue', edgecolor='black')
                value.scatter(virginica_arrays[i], virginica_arrays[i+1], label="virginica", color='green', edgecolor='black')
                value.set_title('\nwith best fit lines per dataset and per species', fontsize=9)
                # Calculate the best fit coefficients for a first order ploynomial (straight line) for the iris dataset

import pandas as pd
df = pd.read_csv("../iris.data", names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

bestfitall = BestFitAll(df)
bestfitall.bestfit_all()