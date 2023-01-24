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
    def __init__(self):
        
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        




        self.world = WORLD()
        self.robot = ROBOT()
        self.Run()
        self.__del__()

    def Run(self):
        for a in range(0,1000):
            p.stepSimulation()
            self.robot.Sense()
            self.robot.Act()
            time.sleep(1/600)
            


    def __del__(self):
        p.disconnect()