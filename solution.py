import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
class SOLUTION:
	def __init__(self):
		self.weights = 2*numpy.random.rand(3,2) -1

	def Create_World(self):   
	    pyrosim.Start_SDF("world.sdf")
	    l = 1
	    w = 1
	    h = 1
	    pyrosim.Send_Cube(name="Box", pos = [100,100,1.5], size = [l,w,h])
	    pyrosim.End()

	def Create_Body(self):
	    pyrosim.Start_URDF("body.urdf")
	    l = 1
	    w = 1
	    h = 1
	    pyrosim.Send_Cube(name="Torso", pos = [0,0,1.5], size = [l,w,h])
	    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position =[-0.5,0,1])
	    pyrosim.Send_Cube(name="BackLeg", pos = [-0.5,0,-0.5], size= [l,w,h])
	    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position =[0.5,0,1])
	    pyrosim.Send_Cube(name="FrontLeg", pos = [0.5,0,-0.5], size= [l,w,h])
	    pyrosim.End()

	def Generate_Brain(self):
	    pyrosim.Start_NeuralNetwork("brain.nndf")
	    pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
	    pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
	    pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
	    pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BackLeg")
	    pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_FrontLeg")
	    for currentRow in range(0,2):
	    	for currentColumn in range (0,1):
	    		pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, weight =self.weights[currentRow][currentColumn])
	    # pyrosim.Send_Synapse(sourceNeuronName = 0, targetNeuronName = 4, weight = 3.0)
	    # pyrosim.Send_Synapse(sourceNeuronName = 1, targetNeuronName = 4, weight = 15.0)
	    # pyrosim.Send_Synapse(sourceNeuronName = 2, targetNeuronName = 4, weight = 3.0)
	    # pyrosim.Send_Synapse(sourceNeuronName = 0, targetNeuronName = 3, weight = 0.2)
	    pyrosim.End()

	def Evaluate(self, dOrG):
		self.Create_World()
		self.Create_Body()
		self.Generate_Brain()
		os.system("python3 simulate.py " + dOrG)
		f = open("fitness.txt", "r")
		self.fitness = float(f.read())
		f.close()

	def Mutate(self):
		self.weights[random.randint(0,2)][random.randint(0,1)] = random.random()*2 -1
