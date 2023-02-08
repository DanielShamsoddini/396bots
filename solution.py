import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
import pybullet as p
import pybullet_data


class SOLUTION:
	def __init__(self, nextav):
		self.weights = 2*numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) -1
		self.myID = nextav

	def Create_World(self):   
	    pyrosim.Start_SDF("world.sdf")
	    l = 1
	    w = 1
	    h = 1
	    pyrosim.Send_Cube(name="Box", pos = [5,5,1.5], size = [l,w,h])
	    pyrosim.Send_Cube(name="Box2", pos = [10,15,1.5], size = [l,w,h])
	    pyrosim.Send_Cube(name="Box3", pos = [10,5,1.5], size = [l,w,h])
	    pyrosim.Send_Cube(name="Box4", pos = [2,4,5.5], size = [1.5*l,1.5*w,5*h])
	    pyrosim.Send_Cube(name="Bo5", pos = [20,20,1.5], size = [l,w,h])
	    pyrosim.End()

	def Create_Body(self):
	    pyrosim.Start_URDF("body.urdf")
	    l = 0.1
	    w = 0.4
	    h = 0.1
	    pyrosim.Send_Cube(name="Torso", pos = [0,0,1.5], size = [1,0.8,0.5])
	    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position =[0.5,0.5,1], jointAxis = "0 1 0")
	    pyrosim.Send_Cube(name="FrontLeg", pos = [0,0.1,0], size= [l,h,w])
	    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position =[0,-0.5,1], jointAxis = "0 1 0")
	    pyrosim.Send_Cube(name="BackLeg", pos = [-0.5,-0.1,0], size= [l,h,w])
	    pyrosim.Send_Joint( name = "Torso_UpLeg" , parent= "Torso" , child = "UpLeg" , type = "revolute", position =[0, 1,1], jointAxis = "0 1 0")
	    pyrosim.Send_Cube(name="UpLeg", pos = [-0.5, 0,0], size= [l,h,w])
	    pyrosim.Send_Joint( name = "Torso_DownLeg" , parent= "Torso" , child = "DownLeg" , type = "revolute", position =[0,-1,1], jointAxis = "0 1 0")
	    pyrosim.Send_Cube(name="DownLeg", pos = [0.5,0,0], size= [l,h,w])
	    pyrosim.Send_Cube(name="Head", pos = [0.1,0, 0.5], size = [0.2,0.2,0.2])
	    pyrosim.Send_Joint(name = "Torso_Head", parent = "Torso", child = "Head", type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
	    
	    
	    pyrosim.End()

	def Generate_Brain(self):
	    pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
	    pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
	    pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
	    pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
	    pyrosim.Send_Sensor_Neuron(name = 3, linkName = "UpLeg")
	    pyrosim.Send_Sensor_Neuron(name = 4, linkName = "DownLeg")
	    pyrosim.Send_Motor_Neuron(name = 5, jointName = "Torso_BackLeg")
	    pyrosim.Send_Motor_Neuron(name = 6, jointName = "Torso_FrontLeg")
	    pyrosim.Send_Motor_Neuron(name = 7, jointName = "Torso_UpLeg")
	    pyrosim.Send_Motor_Neuron(name = 8, jointName = "Torso_DownLeg")
	    #pyrosim.Send_Sensor_Neuron(name = 9, linkName = "Head")
	    
	    for currentRow in range(0,c.numSensorNeurons):
	    	for currentColumn in range (0,c.numMotorNeurons):
	    		pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = random.randint(5,8), weight =self.weights[currentRow][currentColumn])
	    # pyrosim.Send_Synapse(sourceNeuronName = 0, targetNeuronName = 4, weight = 3.0)
	    # pyrosim.Send_Synapse(sourceNeuronName = 1, targetNeuronName = 4, weight = 15.0)
	    # pyrosim.Send_Synapse(sourceNeuronName = 2, targetNeuronName = 4, weight = 3.0)
	    # pyrosim.Send_Synapse(sourceNeuronName = 0, targetNeuronName = 3, weight = 0.2)
	    pyrosim.End()

	#def Evaluate(self, dOrG):
		
	def Start_Simulation(self, dOrG):
		self.Create_World()
		self.Create_Body()
		self.Generate_Brain()

		# while not os.path.exists("world.sdf"):
		# 	time.sleep(0.01)
		# while not os.path.exists("body.urdf"):
		# 	time.sleep(0.01)
		# while not os.path.exists("brain.nndf"):
		# 	time.sleep(0.01)
		os.system("python3 simulate.py " + dOrG +" "+str(self.myID)+
                          #" 2&>1"+
                          " &")
		
		
	def Wait_For_Simulation_To_End(self):
		while not os.path.exists("fitness" + str(self.myID)+".txt"):
			time.sleep(0.01)
		f = open("fitness" + str(self.myID)+".txt", "r")
		self.fitness = float(f.read())
		#print(self.fitness)
		f.close()
		os.system("rm " + "fitness" + str(self.myID)+".txt")

	def Mutate(self):
		self.weights[random.randint(0,c.numSensorNeurons-1)][random.randint(0,c.numMotorNeurons-1)] = (random.random()*2) -1

	def Set_ID(self, numb):
		self.myID = numb
