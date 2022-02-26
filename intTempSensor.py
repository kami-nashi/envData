import time
import board
import adafruit_htu31d
import datetime

i2c = board.I2C()  # uses board.SCL and board.SDA
htu = adafruit_htu31d.HTU31D(i2c)
htu.heater = False

temperature, relative_humidity = htu.measurements
tempF = (temperature * 9/5) + 32
currentTime = datetime.datetime.now()

print(str(currentTime) + ",", str(tempF) + ",", str(relative_humidity))

#returns
#2022-02-26 09:58:27.106682, 56.158480201419096, 44.576180666819255
