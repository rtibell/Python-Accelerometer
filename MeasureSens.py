from sense_hat import SenseHat
from time import sleep
import numpy as np
import math
import time

class MeasureSens:
    G_CONST=9.82
    ACC_DIV=1
    RUCK_DIV=1
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
        self.dsp_mtx = np.zeros((8,8),dtype='i,i,i') 
        print("prt-1", self.dsp_mtx)
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
          print("prt-2", "tm {0}   x {1}  y {2}  z {3}  acc {4} delta {5}".format(tm, x, y, z, tacc, ruck))
          self.display_matrix()

    def display_matrix(self):
        #print("prt-2", self.dsp_mtx)
        self.dsp_mtx = np.roll(self.dsp_mtx, -1)
        #print("prt-3", self.dsp_mtx)
        red_mtx = np.delete(self.dsp_mtx, 7, axis=1)
        #print("prt-4", red_mtx)
        last_column = [ self.set_color(xx,
                                     self.buff[self.idx][self.IDX_TACC],
                                     self.buff[self.idx][self.IDX_RUCK]
                                 ) for xx in range(0,8)]
        #print("prt-5", last_column)
        tmp_array = np.array(last_column, dtype='i,i,i')
        #tmp_array = np.matrix(last_column, dtype='i,i,i')
        #print("prt-6", tmp_array)
        #last_column = tmp_array.transpose()
        last_column = tmp_array.reshape(8,1)
        #print("prt-7", last_column, type(last_column))
        self.dsp_mtx = np.append(red_mtx, last_column, axis=1)
        #np.hstack((self.dsp_mtx, last_column))
        #print("prt-8", self.dsp_mtx, type(self.dsp_mtx))
        dsp_buff = self.dsp_mtx.ravel()
        #print("prt-9", dsp_buff, type(dsp_buff))
        self.sense.set_pixels(dsp_buff)
        
    def set_color(self, x, acc, ruck):
        #print("prt-10", x, acc, ruck)
        norm_acc = int((abs((acc * 10) - self.G_CONST) * 100) // self.ACC_DIV)
        #print("prt-10", x, acc, norm_acc, self.ACC_DIV)
        if (norm_acc > 7):
            self.ACC_DIV = int((abs((acc * 10) - self.G_CONST) * 100) // 7)
            print("prt-10 new", self.ACC_DIV)
            return self.set_color(x, acc, ruck)
        norm_ruck = int((ruck * 100) // self.RUCK_DIV)
        #print("prt-11", x, ruck, norm_ruck, self.RUCK_DIV)
        if (norm_ruck > 255):
            self.RUCK_DIV = int((ruck * 100) // 255)
            print("prt-11 new", self.RUCK_DIV)
            return self.set_color(x, acc, ruck)
        print("prt-12", norm_acc, norm_ruck, self.ACC_DIV, self.RUCK_DIV)
        if (x < norm_acc):
            return (20, norm_ruck, norm_acc * 30)
        else:
            return (3, 3, 3)
        

    def loop(self):
        while True:
            self.measure_acceleration()

ms = MeasureSens()
ms.loop()
