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

def get_colour(rgb):
  (r, g, b) = rgb
  r = r + 4
  if (r > 255):
    r = 0
    g = g + 4
  if (g > 255):
    g = 0
    b = b + 4
  if (b > 255):
    r = g = b = 0
  return (r, g, b)

def rand_coord():
  return randint(0,7)

mod=0
rgb = (0, 0, 0)
sense.clear()

for x in range(100000):
  rgb = get_colour(rgb)
  #c = (x // 8) % 8
  #r = x % 8
  r = rand_coord()
  c = rand_coord()
  sense.set_pixel(r, c, rgb)
  #sleep(0.005)

sleep(3)
sense.clear()

