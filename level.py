import time
import math
from adafruit_circuitplayground.express import cpx

def yx_angle(y, x):
    if x == 0.0:
        anglex = 90
    else:
        # compute the x/y angle from vertical
        anglex = math.atan(y/x)*180/math.pi
    return anglex

def zy_angle(z, y):
    if y == 0.0:
        angley = 90
    else:
        # compute the x/y angle from vertical
        angley = math.atan(z/y)*180/math.pi
    return angley

def zx_angle(z, x):
    if x == 0.0:
        anglez = 90
    else:
        # compute the x/y angle from vertical
        anglez = math.atan(z/x)*180/math.pi
    return anglez

mode = 0

while True:
    sumx = 0
    sumy = 0
    sumz = 0
    lastx = 0
    lastz = 0
    lasty = 0
    for i in range(0, 30, 1):
        x, y, z = cpx.acceleration
        if(i == 0):
            lastx = x
            lasty = y
            lastz = z
        if(abs(x - lastx) > 5):
            i -= 1
        elif(abs(z - lastz) > 5):
            i -= 1
        elif(abs(y - lasty) > 5):
            i -= 1
        else:
            sumx += x
            sumy += y
            sumz += z
            lastx = x
            lasty = y
            lastz = z
        time.sleep(0.01)
    x = sumx/30
    y = sumy/30
    z = sumz/30
    time.sleep(0.1)
    if cpx.button_a:
        mode+=1
    elif cpx.button_b:
        mode -= 1

    if(mode > 2):
        mode = 2
    elif(mode < 0):
        mode = 0
    if(mode == 0):
        angle = yx_angle(y, x)
        red = 255 * (1 - (abs(angle)/90))
        green = 0
        blue = 255 * (1 - (abs(angle)/90))
    elif(mode == 1):
        angle = zx_angle(z, x)
        red = 0
        green = 0
        blue = 255 * (1 - (abs(angle)/90))
    elif(mode == 2):
        angle = zy_angle(z, y)
        red = 255 * (1 - (abs(angle)/90))
        green = 0
        blue = 0

    cpx.pixels.brightness = 0.1
    if abs(angle)< 1.5:
        cpx.pixels.fill((0,150,0))
        #time.sleep(1.0)
    else:
        cpx.pixels.fill((red, green, blue))
        print("Angle: " + str(angle))
    sleep = 0.1 - (abs(math.sin(abs(angle))) * 0.1)
    print("Sleep: " + str(sleep))
    time.sleep(sleep)
