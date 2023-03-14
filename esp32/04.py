import esp32
while True:
  tf = esp32.raw_temperature()
  sn=esp32.hall_sensor()
  print(tf)
  print(sn)
