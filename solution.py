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
		self.weights = 2*numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) - 1
		self.myID = nextav
		self.a = numpy.zeros((c.numSensorNeurons, c.numMotorNeurons))
		self.randlength = random.randint(2,c.randlen-1)

	def Create_World(self):
		pyrosim.Start_SDF("world"+str(self.myID)+".sdf")
		l = 1
		w = 1
		h = 1
		# pyrosim.Send_Cube(name="Box", pos = [5,5,1.5], size = [l,w,h])
		# pyrosim.Send_Cube(name="Box2", pos = [10,15,1.5], size = [l,w,h])
		# pyrosim.Send_Cube(name="Box3", pos = [10,5,1.5], size = [l,w,h])
		# #pyrosim.Send_Cube(name="Box4", pos = [2,4,5.5], size = [1.5*l,1.5*w,5*h])
		# pyrosim.Send_Cube(name="Bo5", pos = [20,20,1.5], size = [l,w,h])
		pyrosim.End()

	def poscalculator(self, currentIndex, blocksize = [0,0,0]):
		if blocksize is [0,0,0]:
			return [0,0,1]
		else:
			return [0, blocksize[1], blocksize[2]/2]
		
	
	def randsize(self):
		return [random.uniform(c.minsize, c.maxsize), random.uniform(c.minsize, c.maxsize), random.uniform(c.minsize, c.maxsize)]

	def Create_Body(self):
		pyrosim.Start_URDF("body"+str(self.myID)+".urdf")
		l = 0.1
		w = 0.4
		h = 0.1
		#pyrosim.Send_Cube(name = "Box4", pos = [5,10,5], size = [1,1,5])
		tempsize = self.randsize()
		tempsize2 = self.randsize()
		tempsize3 = self.randsize()
		tempsize4 = self.randsize()

		tempsize = [self.randsize() for a in range(self.randlength+1)]
		pyrosim.Send_Cube(name = "Box0", pos = [0,0,1], size = tempsize[0])
		for a in range(1,self.randlength+1):
			pyrosim.Send_Joint(name = "Box"+str(a-1)+"_Box"+str(a), parent = "Box"+str(a-1) , child = "Box"+str(a), type = "revolute", position = [0, (tempsize[a-1][1] + tempsize[a][1])/2.0, 0], jointAxis = "1 0 0")
			pyrosim.Send_Cube(name = "Box"+str(a), pos = [0,0,1], size = tempsize[a])
		# pyrosim.Send_Cube(name = "Box0", pos = [0,0,1], size = tempsize)
		# pyrosim.Send_Joint(name = "Box0_Box1", parent = "Box0", child = "Box1", type = "revolute", position = [0, (tempsize[1] + tempsize2[1])/2.0, 0], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name = "Box1", pos = [0,0,1], size = tempsize2)
		# pyrosim.Send_Joint(name = "Box1_Box2", parent = "Box1", child = "Box2", type = "revolute", position = [0, (tempsize2[1] + tempsize3[1])/2.0, 0], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name = "Box2", pos = [0,0,1], size = tempsize3)
		# pyrosim.Send_Joint(name = "Box2_Box3", parent = "Box2", child = "Box3", type = "revolute", position = [0, (tempsize3[1] + tempsize4[1])/2.0, 0], jointAxis = "1 0 0")
		# pyrosim.Send_Cube(name = "Box3", pos = [0,0,1], size = tempsize4)
		# for a in range(1, self.randlength):
		# 	sizee = self.randsize()
			
		# 	pyrosim.Send_Joint(name = "Box"+str(a)+"_"+"Box"+str(a+1), parent = "Box"+str(a), child = "Box"+str(a+1), type = "revolute", position = self.poscalculator(a), jointAxis = "1 0 0")
		# 	pyrosim.Send_Cube(name = "Box"+str(a+1), pos = self.poscalculator(a, blocksize = sizee), size = sizee)
			
			
		
#       pyrosim.Send_Cube(name="Torso", pos = [0,0,1.4], size = [1,1,0.5])
#       pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position =[0.4,0.5,1], jointAxis = "1 0 0")
#       pyrosim.Send_Cube(name="FrontLeg", pos = [0,0,0], size= [l,h,w])
#       pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position =[0,-0.5,1], jointAxis = "1 0 0")
#       pyrosim.Send_Cube(name="BackLeg", pos = [-0.4,-0,0], size= [l,h,w])
#       pyrosim.Send_Joint( name = "Torso_UpLeg" , parent= "Torso" , child = "UpLeg" , type = "revolute", position =[0, 0.5,1], jointAxis = "1 0 0")
#       pyrosim.Send_Cube(name="UpLeg", pos = [-0.4, 0,0], size= [l,h,w])
#       pyrosim.Send_Joint( name = "Torso_DownLeg" , parent= "Torso" , child = "DownLeg" , type = "revolute", position =[0,-0.5,1], jointAxis = "1 0 0")
#       pyrosim.Send_Cube(name="DownLeg", pos = [0.4,0,0], size= [l,h,w])
#       pyrosim.Send_Cube(name="Head", pos = [-0.5,0.6, 0.5], size = [0.2,0.2,0.4])
#       pyrosim.Send_Joint(name = "Torso_Head", parent = "Torso", child = "Head", type = "revolute", position = [0.5,0,1], jointAxis = "0 1 0")
		pyrosim.End()

	def targnname(self, finalorno,x,y):
		if finalorno:
			z = int(random.randint(5,8))
			#print(self.a[x][y])
			self.a[x][y] = z
			return z
		else:
			return self.a[x][y]
   
   
	def Generate_Brain(self,finalorno):
		pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
		neurontracker = 0
		for a in range(0, self.randlength):
			if random.randint(1, 6) < c.odds:
				pyrosim.Send_Sensor_Neuron(name = neurontracker, linkName = "Box"+str(a))
				neurontracker = neurontracker + 1
			pyrosim.Send_Motor_Neuron(name = neurontracker, jointName = "Box"+str(a)+"_"+"Box"+str(a+1))
			neurontracker = neurontracker + 1
		
#       pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
#       pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
#       pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
#       pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
#       pyrosim.Send_Sensor_Neuron(name = 3, linkName = "UpLeg")
#       pyrosim.Send_Sensor_Neuron(name = 4, linkName = "DownLeg")
#       pyrosim.Send_Motor_Neuron(name = 5, jointName = "Torso_BackLeg")
#       pyrosim.Send_Motor_Neuron(name = 6, jointName = "Torso_FrontLeg")
#       pyrosim.Send_Motor_Neuron(name = 7, jointName = "Torso_UpLeg")
#       pyrosim.Send_Motor_Neuron(name = 8, jointName = "Torso_DownLeg")
#       #pyrosim.Send_Sensor_Neuron(name = 9, linkName = "Head")
#
#       for currentRow in range(0,c.numSensorNeurons):
#           for currentColumn in range (0,c.numMotorNeurons):
#               pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = random.randint(5,8), weight =self.weights[currentRow][currentColumn])
#       # pyrosim.Send_Synapse(sourceNeuronName = 0, targetNeuronName = 4, weight = 3.0)
#       # pyrosim.Send_Synapse(sourceNeuronName = 1, targetNeuronName = 4, weight = 15.0)
#       # pyrosim.Send_Synapse(sourceNeuronName = 2, targetNeuronName = 4, weight = 3.0)
#       # pyrosim.Send_Synapse(sourceNeuronName = 0, targetNeuronName = 3, weight = 0.2)
		pyrosim.End()

	#def Evaluate(self, dOrG):

	def Start_Simulation(self, dOrG):
		self.Create_World()
		#self.Create_Body()
		self.Create_Body()
		self.Generate_Brain(True)

		# while not os.path.exists("world.sdf"):
		#   time.sleep(0.01)
		# while not os.path.exists("body.urdf"):
		#   time.sleep(0.01)
		# while not os.path.exists("brain.nndf"):
		#   time.sleep(0.01)
		os.system("python3 simulate.py " + dOrG +" "+str(self.myID)+
						  #" 2&>1"+
						  " &")

	def Best_Simulation(self, dOrG):
		self.Create_World()
		self.Create_Body()
		self.Generate_Brain(False)

		# while not os.path.exists("world.sdf"):
		#   time.sleep(0.01)
		# while not os.path.exists("body.urdf"):
		#   time.sleep(0.01)
		# while not os.path.exists("brain.nndf"):
		#   time.sleep(0.01)
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
		os.system("rm body*.urdf")

	def Mutate(self):
		self.weights[random.randint(0,c.numSensorNeurons-1)][random.randint(0,c.numMotorNeurons-1)] = (random.random()*2) - 1

	def Set_ID(self, numb):
		self.myID = numb
