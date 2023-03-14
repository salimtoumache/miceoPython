from machine import Pin
from utime import sleep_ms
led=Pin(21,Pin.OUT)
while True:
  led.on()
  sleep_ms(500)
  led.off()
  sleep_ms(500)