import matplotlib.pyplot as plt
import requests
import json
import os
import datetime
from cache import load_cache, save_cache
from weather import is_cache_valid, extract_weather_data
from temperature_trend import plot_temperature_twoInOne
import time
from weather import get_weather

API_KEY = '6b03a86116c4bfcfeb0a1c66bd5f92bc'
def get_weather_data(city):
    # cache_data = load_cache()
    # if city in cache_data:
    #     weather_data_variable = cache_data[city]
    # return weather_data_variable
    cache_data = load_cache()

    if city in cache_data:
        weather_data_variable = cache_data[city]
        if is_cache_valid(weather_data_variable):
            return weather_data_variable

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    

    if data["cod"] == "404":
        print(f"City '{city}' not found. Please check the spelling.")
        return

    if data["cod"] == "401":
        print(f"API Key is not working. Try again later.")
        return

    weather_data_variable = extract_weather_data(data)
    cache_data[city] = weather_data_variable
    save_cache(cache_data)
    print("\n")
    capitalized = city.capitalize()
    # print(f"{capitalized}'s Weather Tale Unfolds... \n")
    
    return weather_data_variable
        
def compare_weather(city1, weather_data_city1, city2, weather_data_city2):
    # Call the function from the other file that plots the temperature graph
    plot_temperature_twoInOne(weather_data_city1, city1, weather_data_city2, city2 )
    return