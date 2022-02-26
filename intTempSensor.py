import time
import board
import adafruit_htu31d

i2c = board.I2C()  # uses board.SCL and board.SDA
htu = adafruit_htu31d.HTU31D(i2c)
#does not work out of box anymore
#will delete this soon
#print("Found HTU31D with serial number", hex(htu.serial_number))

#won't be using heater on this project, make sure its off
#htu.heater = True
#print("Heater is on?", htu.heater)
htu.heater = False
#print("Heater is on?", htu.heater)

temperature, relative_humidity = htu.measurements
tempF = (temperature * 9/5) + 32
print("Temperature: %0.1f F" % tempF)
print("Humidity: %0.1f %%" % relative_humidity)
print("")
time.sleep(1)

