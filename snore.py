# Nathan Moore
# starting from from adafruit example
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import board
import digitalio
import time

# set up the (red) LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
T_fast = 0.01
bright = 0.8
up = False

while True:
    T_on = bright*T_fast
    T_off = (1-bright)*T_fast
    led.value = True
    time.sleep(T_on)
    led.value = False
    time.sleep(T_off)
    if(up):
        bright += 0.001
    else:
        bright -= 0.001
    if(bright <= 0.1):
        bright = 0.1
        up = True
    elif(bright >= 0.8):
        bright = 0.8
        up = False
