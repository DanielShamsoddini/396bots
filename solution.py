import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c


class SOLUTION:
	def __init__(self, nextav):
		self.weights = 2*numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) -1
		self.myID = nextav

	def Create_World(self):   
	    pyrosim.Start_SDF("world.sdf")
	    l = 1
	    w = 1
	    h = 1
	    pyrosim.Send_Cube(name="Box", pos = [100,100,1.5], size = [l,w,h])
	    pyrosim.End()

	def Create_Body(self):
	    pyrosim.Start_URDF("body.urdf")
	    l = 0.2
	    w = 1
	    h = 0.2
	    pyrosim.Send_Cube(name="Torso", pos = [0,0,1], size = [1,1,1])
	    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position =[0,0.5,1], jointAxis = "1 0 0")
	    pyrosim.Send_Cube(name="FrontLeg", pos = [0,0.5,0], size= [l,w,h])
	    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position =[0,-0.5,1], jointAxis = "1 0 0")
	    pyrosim.Send_Cube(name="BackLeg", pos = [0,-0.5,0], size= [l,w,h])
	    pyrosim.Send_Joint( name = "Torso_UpLeg" , parent= "Torso" , child = "UpLeg" , type = "revolute", position =[-0.5, 0,1], jointAxis = "0 1 0")
	    pyrosim.Send_Cube(name="UpLeg", pos = [-0.5, 0,0], size= [w,l,h])
	    pyrosim.Send_Joint( name = "Torso_DownLeg" , parent= "Torso" , child = "DownLeg" , type = "revolute", position =[0.5,0,1], jointAxis = "0 1 0")
	    pyrosim.Send_Cube(name="DownLeg", pos = [0.5,0,0], size= [w,l,h])
	    pyrosim.Send_Joint( name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position =[0,1,0], jointAxis = "0 1 0")
	    pyrosim.Send_Cube(name="FrontLowerLeg", pos = [0,0,-0.5], size= [l,h,w])
	    pyrosim.Send_Joint( name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position =[0,-1,0], jointAxis = "0 1 0")
	    pyrosim.Send_Cube(name="BackLowerLeg", pos = [0,0,-0.5], size= [l,h,w])
	    pyrosim.Send_Joint( name = "UpLeg_UpLowerLeg" , parent= "UpLeg" , child = "UpLowerLeg" , type = "revolute", position =[-1,0,0], jointAxis = "0 1 0")
	    pyrosim.Send_Cube(name="UpLowerLeg", pos = [0,0,-0.5], size= [l,h,w])
	    pyrosim.Send_Joint( name = "DownLeg_DownLowerLeg" , parent= "DownLeg" , child = "DownLowerLeg" , type = "revolute", position =[1,0,0], jointAxis = "0 1 0")
	    pyrosim.Send_Cube(name="DownLowerLeg", pos = [0,0,-0.5], size= [l,h,w])
	    
	    
	    pyrosim.End()

	def Generate_Brain(self):
	    pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
	    pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
	    pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
	    pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
	    pyrosim.Send_Sensor_Neuron(name = 3, linkName = "UpLeg")
	    pyrosim.Send_Sensor_Neuron(name = 4, linkName = "DownLeg")
	    pyrosim.Send_Sensor_Neuron(name = 5, linkName = "FrontLowerLeg")
	    pyrosim.Send_Sensor_Neuron(name = 6, linkName = "DownLowerLeg")
	    pyrosim.Send_Sensor_Neuron(name = 7, linkName = "BackLowerLeg")
	    pyrosim.Send_Sensor_Neuron(name = 8, linkName = "UpLowerLeg")
	    pyrosim.Send_Motor_Neuron(name = 9, jointName = "Torso_BackLeg")
	    pyrosim.Send_Motor_Neuron(name = 10, jointName = "Torso_FrontLeg")
	    pyrosim.Send_Motor_Neuron(name = 11, jointName = "Torso_UpLeg")
	    pyrosim.Send_Motor_Neuron(name = 12, jointName = "Torso_DownLeg")
	    
	    for currentRow in range(0,c.numSensorNeurons):
	    	for currentColumn in range (0,c.numMotorNeurons):
	    		pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = random.randint(9,12), weight =self.weights[currentRow][currentColumn])
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
		os.system("python3 simulate.py " + dOrG +" "+str(self.myID)+" 2&>1" +" &")
		
		
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
