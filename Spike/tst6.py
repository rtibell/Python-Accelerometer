from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

def rand_colour():
  return randint(0,2) * 32

# Generate a random colour
def pick_random_colour():
  random_red = rand_colour()
  random_green = rand_colour()
  random_blue = rand_colour()
  if (randint(0,7) == 0):
    return (0,0,0)
  return (random_red, random_green, random_blue)

def rand_coord():
  return randint(0,7)

sense.clear()
for x in range(8*8*16):
  r = rand_coord()
  c = rand_coord()
  sense.set_pixel(r, c, pick_random_colour())
  sleep(0.01)

sleep(3)
sense.clear()

