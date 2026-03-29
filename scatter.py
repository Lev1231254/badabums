import matplotlib.pyplot as plt
import numpy as np
from irisClass import Iris

# plots a scatter graph using following parameters as x and y axes

# 0 is 'Sepal length'
# 1 is 'Sepal width'
# 2 is 'Petal length'
# 3 is 'Petal width'

def plotScatter(setosas : Iris, versicolors : Iris, virginicas : Iris, parameters : tuple):

    print([row[parameters[0]] for row in setosas.data])

    setosasX = [float(row[parameters[0]]) for row in setosas.data]
    setosasY = [float(row[parameters[1]]) for row in setosas.data]
    versicolorsX = [float(row[parameters[0]]) for row in versicolors.data]
    versicolorsY = [float(row[parameters[1]]) for row in versicolors.data]
    virginicasX = [float(row[parameters[0]]) for row in virginicas.data]
    virginicasY = [float(row[parameters[1]]) for row in virginicas.data]

    plt.scatter(setosasX, setosasY, c = 'blue', alpha = 0.3,
                label = 'Setosas')
    plt.scatter(versicolorsX, versicolorsY, c = 'red', alpha = 0.3,
                label = 'Versicolors')
    plt.scatter(virginicasX, virginicasY, c = 'green', alpha = 0.3,
                label = 'Virginicas')


    attributes = ['Sepal length','Sepal width','Petal length','Petal width']
    title = 'Relationship between ' + attributes[parameters[0]] + ' and ' + attributes[parameters[1]]
    plt.title(title, fontweight = 'bold')
    plt.xlabel(attributes[parameters[0]], fontweight = 'bold')
    plt.ylabel(attributes[parameters[1]], fontweight = 'bold')

    plt.legend()
    plt.show()
