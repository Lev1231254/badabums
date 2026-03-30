import matplotlib.pyplot as plt
import numpy as np
from irisClass import Iris


def plotAverages(setosas : Iris, versicolors : Iris, virginicas : Iris):
    barWidth = 0.25
    fig = plt.subplots(figsize=(12, 8))
    
    br1 = np.arange(4)
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]


    # plot
    plt.bar(br1, setosas.averages, color = 'r', width = barWidth,
        edgecolor = 'grey', label = 'Setosas')
    plt.bar(br2, versicolors.averages, color = 'b', width = barWidth,
        edgecolor = 'grey', label = 'Versicolors')
    plt.bar(br3, virginicas.averages, color = 'g', width = barWidth,
        edgecolor = 'grey', label = 'Virginicas')


    # decorate
    plt.ylabel('Length/width in cm', fontweight = 'bold')

    plt.xticks([x + barWidth for x in range(4)],
               ['Sepal length','Sepal width','Petal length','Petal width'])

    plt.legend()

    plt.show()