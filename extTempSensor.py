import requests
import json
import datetime

# API key API_KEY = "Your API Key"
URL = 'https://api.openweathermap.org/data/2.5/weather?q=fayetteville,us&APPID=' + API_KEY + '&units=imperial'
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   currentTime = datetime.datetime.now()
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperature = main['temp']
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # weather report
   report = data['weather']
   #print(f"Temperature: {temperature}")
   #print(f"Humidity: {humidity}")
   print(str(currentTime) + ",", str(temperature) + ",", str(humidity))
else:
   # showing the error message
   print("Error in the HTTP request")
