import requests
import datetime
from input_check import inputCheck
from bs4 import BeautifulSoup
from auth_data import weather_token


class Weather_data:
    def get_weatherData(self,city):
#Trying to get data from openweather and then takes data in json format
       try: 
           req=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric")
           data=req.json()
           cur_weather=data['weather'][0]['main']
           cur_temp=data['main']['temp']
           humidity=data['main']['humidity']
           pressure=data['main']['pressure']
           wind=data['wind']['speed']
           sunrise=datetime.datetime.fromtimestamp(data['sys']['sunrise'])
           sunset=datetime.datetime.fromtimestamp(data['sys']['sunset'])
           meta_data=f"""
<b>Weather</b> : {cur_weather} 
<b>Temperature</b> : {cur_temp} Cel.
<b>Humidity</b> : {humidity}
<b>Pressure</b> : {pressure}
<b>Wind</b> : {wind}
<b>Sunrise</b> : {sunrise}
<b>Sunset</b> : {sunset}
"""
           return meta_data
           
       except Exception as ex:
           print(ex)
           print("Check City Name")


def main(city, country):
    city=inputCheck(city, country)
    Weahter=Weather_data()
    answer="Check City or Country you've typed"
    if city !=None:
        answer=Weahter.get_weatherData(city)
    else:
        print("Check City or Country you've typed") 
    return answer 
