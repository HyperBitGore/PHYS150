from adafruit_circuitplayground import cp
import time
import math

cp.pixels.brightness = .2
grav = 9.8
c = 0;
last = 0
total = 0;
while True:
    x, y, z = cp.acceleration
    r = int(abs(x / grav * 127))
    g = int(abs(y / grav * 127))
    b = int(abs(z / grav * 127))
    cp.pixels.fill([r, g, b])
    if(abs(y) > 0):
        theta_yz = (360/(2.0 * math.pi))*math.atan(z/y)
        #print("yz angle: " + str(theta_yz))
    #else:
        #print("yz: 90 degrees")
        #print("level achieved")
        #time.sleep(4.0)
    if(abs(x) > 0):
        theta_xy = (360/(2.0 * math.pi))*math.atan(y/x)
        theta_xz = (360/(2.0 * math.pi))*math.atan(z/x)
        #print("xy angle: " + str(theta_xy));
        if(abs(last - theta_xy) < 10):
            total += theta_xy
            c+=1
        last = theta_xy
        #print("xz angle: " + str(theta_xz))
    #else:
        #print("xy: 90 degrees; xz: 90 degrees")
        #print("level achieved")
        #time.sleep(4.0)

    if (c >= 10):
        total = total / c
        print("xy angle: " + str(total))
        total = 0
        c = 0

    time.sleep(0.01)
