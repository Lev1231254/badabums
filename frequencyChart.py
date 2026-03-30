from irisClass import Iris
import matplotlib.pyplot as plt


def plotParametersChart(spieces : Iris, parameter : int):

    values = [float(row[parameter]) for row in spieces.data]

    # plot
    plt.hist(values, color = 'pink', edgecolor = 'black', align = 'mid',
             bins = 10)


    # decorate
    parameterName = ['Sepal length','Sepal width','Petal length','Petal width'][parameter] 
    yLabel = 'Frequency'

    plt.xlabel(parameterName, fontweight = 'bold')
    plt.ylabel(yLabel, fontweight = 'bold')
    plt.title(parameterName + ' frequencies', fontweight = 'bold')
    plt.show()





