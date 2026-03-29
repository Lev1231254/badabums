import matplotlib.pyplot as plt
import csv
import numpy as np
from irisClass import Iris
import averages
import scatter

data_file_name = 'Iris-(1).csv'

setosas_data = []
versicolors_data = []
virginicas_data = []


# sort data in 3 chunks
with open(data_file_name, 'r') as data:
    reader = csv.reader(data)
    for row in reader:
        if row[-1] == 'Iris-setosa':
            setosas_data.append(row[1:-1])
        elif row[-1] == 'Iris-versicolor':
            versicolors_data.append(row[1:-1])
        elif row[-1] == 'Iris-virginica':
            virginicas_data.append(row[1:-1])


setosas = Iris('Iris-setosa', setosas_data)
versicolors = Iris('Iris-versicolor', versicolors_data)
virginicas = Iris('Iris-virginicas', virginicas_data)


#averages.plotAverages(setosas, versicolors, virginicas)

scatter.plotScatter(setosas, versicolors, virginicas, (0, 1))