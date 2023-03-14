from machine import Pin,Timer
led=Pin(21,Pin.OUT)
tim0=Timer(0) # timer 1
tim0.init(period=500, mode=Timer.PERIODIC, callback=lambda t:led.value(not led.value()))
# time, mode, fonc
