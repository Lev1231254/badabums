import numpy as np

class Iris:
    #data is SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm
    def __init__(self, species, data):
        self.species = species
        self.data = data


        self.averages = []
        self.averages.append(np.average([float(row[0]) for row in data]))
        self.averages.append(np.average([float(row[1]) for row in data]))
        self.averages.append(np.average([float(row[2]) for row in data]))
        self.averages.append(np.average([float(row[3]) for row in data]))
