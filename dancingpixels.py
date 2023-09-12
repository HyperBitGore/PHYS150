import random
import board
import digitalio
import time
from adafruit_circuitplayground import cp

# set up the (red) LED
#led = digitalio.DigitalInOut(board.D13)
#led.direction = digitalio.Direction.OUTPUT
cp.pixels.brightness = 0.02
cp.pixels.fill((50, 50, 50))

colors = {(255, 50, 50), (25, 255, 25), (25, 25, 255), (150, 150, 50), (150, 50, 150), (50, 150, 150), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)}


speed = 0.1

while True:

    speed = 0.03
    for pn in range(0,10,1):
        col1 = (random.randint(25, 255), random.randint(25, 255), random.randint(25, 255))
        cp.pixels[pn] = col1
        time.sleep(speed)
        speed += 0.01
        cp.pixels[pn] = (0, 0, 0)
    speed = 0.03
    for pn in range(9,-1,-1):
        col1 = (random.randint(25, 255), random.randint(25, 255), random.randint(25, 255))
        cp.pixels[pn] = col1
        time.sleep(speed)
        speed += 0.01
        cp.pixels[pn] = (0, 0, 0)
