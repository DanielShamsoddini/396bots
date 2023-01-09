import pybullet as p
import time
physicsClient = p.connect(p.GUI)
p.loadSDF("box.sdf")
for a in range(0,1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(a)
p.disconnect()
