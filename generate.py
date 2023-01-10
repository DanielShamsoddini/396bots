import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("box.sdf")
l = 1
w = 1
h = 1
pyrosim.Send_Cube(name="Box", pos = [0,0,0.5], size = [l,w,h])
pyrosim.Send_Cube(name="Box2", pos = [1,0,1.5], size = [l,w,h])
pyrosim.End()
