from sense_hat import SenseHat
from time import sleep
import math
import time

sense = SenseHat()
sense.clear()

old_tacc = 0
while True:
  acceleration = sense.get_accelerometer_raw()
  x = acceleration['x']
  y = acceleration['y']
  z = acceleration['z']
  tacc = math.sqrt(x**2 + y**2 + z**2)
  dacc = abs(tacc - old_tacc)
  tm = time.time()
  curr = (tm, x, y, z, tacc, dacc)
  if (dacc > 0.05):
    print("tm {0}   x {1}  y {2}  z {3}  acc {4} delta {5}".format(tm, x, y, z, tacc, dacc))
    old_tacc = tacc
