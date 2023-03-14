from machine import Pin
from time import sleep
led=Pin(2,Pin.OUT)
input_data=Pin(21,Pin.IN)
while True:
  print(input_data.value())
  if input_data.value()==True:
    led.on()
  else:led.off()
  

