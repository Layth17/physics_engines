import pybullet as p
import pybullet_data


physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeID = p.loadURDF("plane.urdf")

p.setGravity(0, 0, -9.8)

while True:
    p.stepSimulation()

if __name__ == '__main__':
    pass