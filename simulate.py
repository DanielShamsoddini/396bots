import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body2.urdf")

#p.loadSDF("world.sdf")
for a in range(0,1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(a)
p.disconnect()
