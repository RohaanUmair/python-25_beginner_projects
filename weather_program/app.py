import requests
from pprint import pprint

API_KEY = ''

city = input('Enter a city: ')

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?appid=' + API_KEY + '&q=' + city

weather_data = requests.get(BASE_URL).json()

pprint(weather_data)