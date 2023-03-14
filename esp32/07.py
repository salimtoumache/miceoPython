from machine import Pin
import time
led=Pin(21,Pin.OUT)
counter=0
while counter<5:
  led.on()
  time.sleep(0.5)
  led.off()
  time.sleep(0.5)
  counter+=1
print("complete")