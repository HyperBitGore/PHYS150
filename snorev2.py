# Nathan Moore
# starting from from adafruit example
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#PWM
import board
import digitalio
import time
import adafruit_irremote
# set up the (red) LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

brightness = 1.0
flip = False
while True:
    # brightness is measured out of a max of 1.0
    T_fast = 0.01
    T_on = brightness*T_fast
    T_off = (1-brightness)*T_fast
    num_repeats=20
    i=0
    while (i<num_repeats):
        led.value = True
        time.sleep(T_on)
        led.value = False
        time.sleep(T_off)
        i=i+1
    if(flip is False):
        brightness -= 0.03
    else:
        brightness += 0.03
    if(brightness <= 0):
        brightness = 0
        flip = True
    elif(brightness >= 1.0):
        brightness = 1.0
        flip = False
    """for brightness in [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]:
        # brightness is measured out of a max of 1.0
        T_fast = 0.01
        T_on = brightness*T_fast
        T_off = (1-brightness)*T_fast
        num_repeats=100
        i=0
        while (i<num_repeats):
            led.value = True
            time.sleep(T_on)
            led.value = False
            time.sleep(T_off)
            i=i+1"""
