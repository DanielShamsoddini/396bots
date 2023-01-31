from world import WORLD
from robot import ROBOT
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random
import constants as c


class SIMULATION:
    def __init__(self, dOrGUI, brainnn):
        self.directOrGUI = dOrGUI
        if self.directOrGUI == "DIRECT":
            physicsClient = p.connect(p.DIRECT)
        elif self.directOrGUI == "GUI":
            physicsClient  = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        




        self.world = WORLD()
        self.robot = ROBOT(brainnn)
        self.Run()
        #self.delee()

    def Run(self):
        sleeptime = 1/600
        if self.directOrGUI == "DIRECT":
            sleeptime = 0
        for a in range(0,1000):
            p.stepSimulation()
            self.robot.Sense()
            self.robot.Think()
            self.robot.Act()
            time.sleep(1/6000)
            


    def delee(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()
