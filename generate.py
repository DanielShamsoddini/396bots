import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("box.sdf")
l = 1
w = 2
h = 3
pyrosim.Send_Cube(name="Box", pos = [0,0,0.5], size = [l,w,h])
pyrosim.End()
