import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
	def __init__(self):
		self.robotId = p.loadURDF("body.urdf")
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		self.nn = NEURAL_NETWORK("brain.nndf")
		
		
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
		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
				desiredAngle = self.nn.Get_Value_Of(neuronName)
				self.motors[jointName].Act(desiredAngle)
				print(jointName)
				print(neuronName)
	def Think(self):
		self.nn.Update()
		self.nn.Print()

