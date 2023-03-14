from machine import Pin
from time import sleep
input_data=Pin(0,Pin.IN)
while True:

  print(input_data.value())
