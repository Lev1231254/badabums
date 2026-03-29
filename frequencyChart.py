from irisClass import Iris
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


def plotFrequencyChart(spieces : Iris, parameter : int):

    barWidth = 0.1
    values = [float(row[parameter]) for row in spieces.data]

    plt.hist(values, color = 'pink', edgecolor = 'black', align = 'mid', rwidth = 0.5)
    plt.show()




