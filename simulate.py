import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)




backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)
for a in range(0,100):
    p.stepSimulation()
    backLegSensorValues[a] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[a] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    time.sleep(1/60)
    
p.disconnect()
print(backLegSensorValues)
numpy.save("data/backLegSensorValues",backLegSensorValues)
numpy.save("data/frontLegSensorValues",frontLegSensorValues)

