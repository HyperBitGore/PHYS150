#Adapted from
#https://learn.adafruit.com/adafruit-lis3dh-triple-axis-accelerometer-breakout/python-circuitpython
#https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage
#https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out
#https://github.com/ntmoore/phys150_fall20/blob/master/10-15_count_steps.py

#not perfect either

import time
import math
from adafruit_circuitplayground.express import cpx
from adafruit_circuitplayground import cp


def flash_leds(start, end, color):
    for i in range(start, end, 1):
        cp.pixels[i] = color
    time.sleep(0.3)
    for i in range(start, end, 1):
        cp.pixels[i] = (0,0, 0)

def total_count(count):
    remaintotal = count / 500

def basic_count(count):
    cur = count % 10
    cp.pixels[cur] = (0, 50, 0)

def count_steps(fp):
    cp.pixels.brightness = 0.05
    #cp.pixels[2]=(0,50,0)
    #cp.pixels[7]=(0,50,0)

    num_steps = 0

    read_delay = 0.2 # how often do we sample acceleration? 0.2 seems good.

    g=9.801
    a_floor = 1.0   # this is the floor that's used in the peak-finiding method

    # setup
    x, y, z = cpx.acceleration
    a0 = math.sqrt(x*x+y*y+z*z)/g
    t0 = time.monotonic()

    x, y, z = cpx.acceleration
    a1 = math.sqrt(x*x+y*y+z*z)/g
    t1 = time.monotonic()

    x, y, z = cpx.acceleration
    a2 = math.sqrt(x*x+y*y+z*z)/g
    t2 = time.monotonic()

    mode = False
    while True:
        #flash_leds(0, 10)
        # fine the (pythagorean) magnitude of acceleration, scaled by g
        x, y, z = cpx.acceleration
        a3 = math.sqrt(x*x+y*y+z*z)/g
        t3 = time.monotonic()

        slope1 = (a1-a0)/(t1-t0)
        slope2 = (a3-a2)/(t3-t2)

        # this is the condition that we worked out in an Excel
        # sheet in class on 2020-10-13
        # A "peak" means the slope changes from positive to negative
        # if the magnitude of acceleration is above some certain
        # minimum value, "a_floor"
        if(
            slope1>0 and slope2<0
            and (a1+a2)*0.5 > a_floor
            ):

            num_steps += 1
            print("peak: ",a0,a1,a2,a3,slope1,slope2,num_steps)
            print(bin(num_steps))

        # update the acceleration and time measurements, ie, move the "window"
        # forward in time
        a0=a1
        a1=a2
        a2=a3
        t0=t1
        t1=t2
        t2=t3

        time.sleep(read_delay)

        if cpx.button_a: #press button a to record the # of steps to "steps.txt"
            mode = False
            time.sleep(0.1)
        elif cpx.button_b:
            mode = True
            time.sleep(0.02)
        if mode == True:
            total_count(num_steps)
        else:
            basic_count(num_steps)


#will try and see if a file is writeable, if it is it continues, if not it goes to the except statement
try:
    #open a file to save the data to
    with open("/steps.txt", "a") as fp:

        cp.pixels[1]=(0,0,50)
        count_steps(fp)

# will flash the D13 red LED to let us know we can edit the code.py file (i.e. the storage is writeable)
except OSError as e:
    delay = 8
    if e.args[0] == 28:
        delay = 4
    cp.pixels[1]=(50,0,0)
    fp=1
    count_steps(fp)
