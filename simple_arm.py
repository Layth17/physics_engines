import pybullet as p
import pybullet_data
import time
import math

# Set up; create empty env
p.connect(p.GUI) # p.DIRECT for non-graphical version
p.resetSimulation() # reset
p.setAdditionalSearchPath(pybullet_data.getDataPath()) # to import assets
p.setGravity(0,0,-9.807) # x,y,z gravity
p.setRealTimeSimulation(0) # r-t simulation


# load; URDF: Universal Robot Description File
p.loadURDF(fileName="plane.urdf", basePosition=[0,0,0], baseOrientation=[0,0,0,1])
object = p.loadURDF(fileName="franka_panda/panda.urdf", basePosition=[0,0,0], baseOrientation=[0,0,0,1], useFixedBase=True)

# for all joints of this object, print info
# but what do the values mean?
# https://github.com/bulletphysics/bullet3/blob/master/examples/pybullet/notebooks/HelloPyBullet.ipynb
for i in range(p.getNumJoints(object)):
    print(p.getJointInfo(object, i))

for step in range(300):
    pos, ori = p.getBasePositionAndOrientation(object)
    # to create a static camera instead of free movement... why, lol?
    # p.resetDebugVisualizerCamera(cameraDistance=3, cameraYaw=3, cameraPitch=-70, cameraTargetPosition=pos)
    p.stepSimulation()
    time.sleep(.01)

if __name__ == '__main__':
    pass