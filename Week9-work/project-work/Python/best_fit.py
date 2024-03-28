import numpy as np
import matplotlib.pyplot as plt

def best_fit(df):
    plen = df['petal_length']

    plen = plen.to_numpy()

    pwdith = df['petal_width']

    pwdith = pwdith.to_numpy()

    #Set the font for the x and y axis labels and the title 
    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    fig, ax = plt.subplots()

    ax.plot(plen, pwdith, 'o', label='Original data', markersize=10)

    m, c = np.polyfit(plen, pwdith, 1)

    ax.plot(plen, m*plen + c, 'r', label='Best fit line')

    ax.set_xlabel('Petal Length (cm)', fontdict=font2)
    ax.set_ylabel('Petal Width (cm)', fontdict=font2)

    plt.title('Best fit line for Petal Length and Petal Width', fontdict=font1)

    plt.legend()

    plt.savefig('Plots/best_fit_line.png')
