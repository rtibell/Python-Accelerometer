from sense_hat import SenseHat
from time import sleep
import math

sense = SenseHat()
sense.clear()

prev_pitch = 0
prev_roll = 0
prev_yaw = 0
while True:
  o = sense.get_orientation()
  pitch = o["pitch"]
  roll = o["roll"]
  yaw = o["yaw"]
  acceleration = sense.get_accelerometer_raw()
  x = acceleration['x']
  y = acceleration['y']
  z = acceleration['z']
  tacc = math.sqrt(x**2 + y**2 + z**2)
  print("pitch {0} [{3}]  roll {1} [{4}]  yaw {2} [{5}]  x {6}  y {7}  z {8}  acc {9}".format(
      round(pitch,0), round(roll,0), round(yaw,0),
      round(pitch - prev_pitch,0), round(roll - prev_roll,0), round(yaw - prev_yaw,0),
      x, y, z, tacc))
  sleep(0.5)
  prev_pitch = pitch
  prev_roll = roll
  prev_yaw = yaw
