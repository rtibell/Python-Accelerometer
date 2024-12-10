from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = (150, 150, 150)
b = (0, 0, 255)
g = (0, 255, 0)
e = (0, 0, 0)

image = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
w,w,w,e,e,g,w,w,
w,w,b,e,e,w,w,b,
w,w,g,e,e,w,w,w,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

sense.set_pixels(image)

while True:
    sleep(1)
    sense.flip_h()
    sleep(1)
    sense.set_rotation(90)
    sleep(1)
    sense.flip_v()
    sleep(1)
    sense.set_rotation(180)
    sleep(1)
    sense.flip_v()
    sleep(1)
    sense.set_rotation(270)
    sleep(1)
    sense.flip_h()
    sleep(1)
    sense.set_rotation(00)
