from machine import Pin
from time import sleep
led = Pin(2,Pin.OUT)
while True:
  led.value(1)
  print(led.value())
  sleep(0.5)
  led.value(0)
  print(led.value())
  sleep(0.5)

  
 
