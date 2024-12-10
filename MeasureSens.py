from sense_hat import SenseHat
from time import sleep
import math
import time

class MeasureSens:
    DELTA_RUCK_CHANGE=0.06
    RING_BUFFER_SIZE=1024
    IDX_TM = 0
    IDX_ACC_X = 1
    IDX_ACC_Y = 2
    IDX_ACC_Z = 3
    IDX_TACC = 4
    IDX_RUCK = 5

    def __init__(self):
        self.sense = SenseHat()
        self.sense.clear()
        self.buff = [[0] * 6] * self.RING_BUFFER_SIZE
        self.buff[0] = [0, 0, 0, 0, 0, 0] # tm, x, y, z, tacc, ruck
        self.idx=0
    
    def measure_acceleration(self):
        next_idx = (self.idx + 1) % self.RING_BUFFER_SIZE # new position in buffer
        acceleration = self.sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']
        tacc = math.sqrt(x**2 + y**2 + z**2)
        ruck = abs(tacc - self.buff[self.idx][self.IDX_TACC])
        tm = time.time()
        if (ruck > self.DELTA_RUCK_CHANGE):
          self.idx = next_idx
          self.buff[self.idx] = [tm, x, y, z, tacc, ruck]
          print("tm {0}   x {1}  y {2}  z {3}  acc {4} delta {5}".format(tm, x, y, z, tacc, ruck))

    def loop(self):
        while True:
            self.measure_acceleration()

ms = MeasureSens()
ms.loop()
