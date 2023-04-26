from machine import Pin
import time

button1 = Pin(28, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(27, Pin.IN, Pin.PULL_DOWN)
code_running = False

def red_val(val, val2):
    red = Pin(18, Pin.OUT)
    red2 = Pin(13, Pin.OUT)
    
    red.value(val)
    red2.value(val2)
    
def white_val(val, val2):
    white = Pin(19, Pin.OUT)
    white2 = Pin(12, Pin.OUT)
    
    white.value(val)
    white2.value(val2)
    
def blue_val(val, val2):
    blue = Pin(20, Pin.OUT)
    blue2 = Pin(11, Pin.OUT)
    
    blue.value(val)
    blue2.value(val2)
    
try:
    while True:
        if button1.value() == 1:
            if code_running == True:
                code_running = False
            else:
                code_running = True
                
        while code_running:
            while button2.value() == 0:                    
                red_val(1, 1)
                white_val(0, 0)
                blue_val(0, 0)

                time.sleep(1)

                red_val(0, 0)
                white_val(1, 1)
                blue_val(0, 0)
                
                time.sleep(1)

                red_val(0, 0)
                white_val(0, 0)
                blue_val(1, 1)
                
                time.sleep(1)
                
                blue_val(0, 0)
                
                time.sleep(1)

                red_val(1, 1)
                white_val(1, 1)
                blue_val(1, 1)
                
                time.sleep(1)

                red_val(0, 0)
                white_val(0, 0)
                blue_val(0, 0)
                
                time.sleep(1)
            code_running = False
    
except KeyboardInterrupt:
    red_val(0, 0)
    white_val(0, 0)
    blue_val(0, 0)