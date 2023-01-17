import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random

amplitudeF = math.pi/4.0
frequencyF = 5
phaseOffsetF = 0
amplitudeB = math.pi/4.0
frequencyB = 5
phaseOffsetB = numpy.pi/4.0
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)




backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
for a in range(0,1000):
    p.stepSimulation()
    backLegSensorValues[a] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[a] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    x1 = numpy.linspace(0*frequencyB+phaseOffsetB,2*numpy.pi*frequencyB+phaseOffsetB,1000)
    x1 = numpy.sin(x1)
    targetAnglesB = numpy.interp(x1, (x1.min(), x1.max()), (-amplitudeB, amplitudeB))
    x2= numpy.linspace(0*frequencyF+phaseOffsetF,2*numpy.pi*frequencyF+phaseOffsetF,1000)
    x2 = numpy.sin(x2)
    targetAnglesF = numpy.interp(x2, (x2.min(), x2.max()), (-amplitudeF, amplitudeF))
    numpy.save("data/targetAnglesB",targetAnglesB)
    numpy.save("data/targetAnglesF",targetAnglesF)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_BackLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesB[a], maxForce = 25)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = "Torso_FrontLeg", controlMode = p.POSITION_CONTROL, targetPosition = targetAnglesF[a], maxForce = 25)

    time.sleep(1/600000000)
    
p.disconnect()
print(backLegSensorValues)
numpy.save("data/backLegSensorValues",backLegSensorValues)
numpy.save("data/frontLegSensorValues",frontLegSensorValues)

