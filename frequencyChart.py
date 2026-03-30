from irisClass import Iris
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


def plotFrequencyChart(spieces : Iris, parameter : int):

    values = [float(row[parameter]) for row in spieces.data]


    # decorations
    plt.hist(values, color = 'pink', edgecolor = 'black', align = 'mid',
             bins = 10)

    parameterName = ['Sepal length','Sepal width','Petal length','Petal width'][parameter] 
    yLabel = 'Frequency'

    plt.xlabel(parameterName, fontweight = 'bold')
    plt.ylabel(yLabel, fontweight = 'bold')
    plt.title(parameterName + ' frequencies', fontweight = 'bold')
    plt.show()




