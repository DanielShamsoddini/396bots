import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import constants as c

class ROBOT:
	def __init__(self):
		self.robotId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		
		
	def Prepare_To_Sense(self):
		self.sensors = {}
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)

	def Sense(self):
		for sensorss in self.sensors:
			self.sensors[sensorss].Get_Value()

	def Prepare_To_Act(self):
		self.motors = {}
		self.amplitude = c.amplitudeB
		self.frequency = c.frequencyB
		self.offset = c.phaseOffsetB
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName,self.robotId, self.amplitude, self.frequency, self.offset)

	def Act(self):
		for jointName in pyrosim.jointNamesToIndices:
			print(jointName)
			print(self.motors.keys())
			self.motors[jointName].Act()


