from sense_hat import SenseHat
from time import sleep
import math
import time

IDX_TM = 0
IDX_ACC_X = 1
IDX_ACC_Y = 2
IDX_ACC_Z = 3
IDX_TACC = 4
IDX_RUCK = 5

sense = SenseHat()
sense.clear()

buff_size=1024
buff = [[0] * 6] * buff_size

buff[0] = [0, 0, 0, 0, 0, 0] # tm, x, y, z, tacc, ruck
old_tacc=0
idx=0
while True:
  idx = (idx + 1) % buff_size
  acceleration = sense.get_accelerometer_raw()
  x = acceleration['x']
  y = acceleration['y']
  z = acceleration['z']
  tacc = math.sqrt(x**2 + y**2 + z**2)
  ruck = abs(tacc - buff[(idx - 1) % buff_size][IDX_TACC])
  tm = time.time()
  buff[idx] = [tm, x, y, z, tacc, ruck]
  if (ruck > 0.05):
    print("tm {0}   x {1}  y {2}  z {3}  acc {4} delta {5}".format(tm, x, y, z, tacc, ruck))
    old_tacc = tacc
