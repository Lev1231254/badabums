from irisClass import Iris
import matplotlib.pyplot as plt


def plotParametersChart(spieces : Iris, parameter : int):

    # prepare data
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



def plotParameterRelationship(species : Iris, parameters : tuple, graphColor : str):

    # prepare data
    relationships = [float(row[parameters[0]]) / float(row[parameters[1]]) for row in species.data]

    # plot
    plt.hist(relationships, color = graphColor, edgecolor = 'grey', label = species.species,
             bins = 10)

    # decorate

    parameterName = ['Sepal length','Sepal width','Petal length','Petal width']
    plt.title('Relationship between ' + parameterName[parameters[0]] + ' and ' + parameterName[parameters[1]])
    plt.xlabel(parameterName[parameters[0]] + ' / ' + parameterName[parameters[1]])
    plt.ylabel('Frequency')

    plt.show()