from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Generate a random colour
def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)


for x in range(8 * 8):
    r = x % 8 
    c = x // 8
    print(r, c)
    sense.set_pixel(r, c, pick_random_colour())
    sleep(0.2)

sense.clear()

