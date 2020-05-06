# Choregraphe bezier export in Python.
from naoqi import ALProxy
import confNAO


names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.76])
keys.append([[0.512314, [3, -0.266667, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.76])
keys.append([[-0.0138481, [3, -0.266667, 0], [3, 0, 0]]])
names.append("LAnklePitch")
times.append([0.76])
keys.append([[-0.354396, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([0.76])
keys.append([[0.00157595, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.76])
keys.append([[-0.987854, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.76])
keys.append([[-1.35456, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.76])
keys.append([[0.262, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([0.76])
keys.append([[-0.454022, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LHipRoll")
times.append([0.76])
keys.append([[-0.0106959, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([0.76])
keys.append([[-0.00455999, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([0.76])
keys.append([[0.707132, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.76])
keys.append([[1.43118, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.76])
keys.append([[0.279146, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.76])
keys.append([[0.0337059, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RAnklePitch")
times.append([0.76])
keys.append([[-0.363516, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RAnkleRoll")
times.append([0.76])
keys.append([[0.00157595, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.76])
keys.append([[0.986404, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.76])
keys.append([[1.36982, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.76])
keys.append([[0.2584, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([0.76])
keys.append([[-0.46331, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([0.76])
keys.append([[0.00771189, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([0.76])
keys.append([[-0.00455999, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([0.76])
keys.append([[0.69341, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.76])
keys.append([[1.4466, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.76])
keys.append([[-0.283832, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.76])
keys.append([[0.0398421, [3, -0.266667, 0], [3, 0, 0]]])

def do():
  try:
    # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  	 motion = ALProxy("ALMotion", confNAO.ip_addr, 9559)
   	# motion = ALProxy("ALMotion")
   	 motion.angleInterpolationBezier(names, times, keys)
  except BaseException, err:
 	 print err
