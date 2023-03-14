from machine import Pin
from time import sleep
led = Pin(2,Pin.OUT)
while True:
  a=int(input("entry:"))
  if a==1:
    led.value(1)
  else:led.value(0)
  
  

  
 
