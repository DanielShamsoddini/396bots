import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
	def __init__(self, jname,rid, amp,freq, phofs):
		self.jointName = jname
		self.robotId = rid
		self.amplitude = amp
		self.frequency = freq
		self.phaseOffset =phofs
		self.a = 0
		self.Prepare_To_Act()

	def Prepare_To_Act(self):
		x1 = numpy.linspace(0*self.frequency+self.phaseOffset,2*numpy.pi* self.frequency+self.phaseOffset,1000)
		x1 = numpy.sin(x1)
		self.targetAngles = numpy.interp(x1, (x1.min(), x1.max()), (-self.amplitude, self.amplitude))
	def Act(self):	
		pyrosim.Set_Motor_For_Joint(bodyIndex = self.robotId, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.targetAngles[self.a], maxForce = 25)
		self.a = self.a + 1

	def Save_Values(self):
		pass