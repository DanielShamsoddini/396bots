import numpy
import matplotlib.pyplot
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
print(backLegSensorValues)
matplotlib.pyplot.plot(backLegSensorValues, linewidth = 5, label = "frontleg")
matplotlib.pyplot.plot(frontLegSensorValues, label = "backleg")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()