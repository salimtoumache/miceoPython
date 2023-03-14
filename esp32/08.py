from machine import Pin
import time
led=Pin(21,Pin.OUT)
def blink_led(max_num,time_on,time_off,msg):

  counter=0
  while counter<max_num:
    led.on()
    time.sleep(time_on)
    led.off()
    time.sleep(time_off)
    counter+=1
  print(msg)
blink_led(5,0.1,0.6,"blink done")