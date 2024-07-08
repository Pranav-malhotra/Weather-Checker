import requests
import datetime
from cache import load_cache, save_cache
from weather_details import print_weather_details
from temperature_trend import plot_temperature_trend
from tqdm import tqdm
import time

API_KEY = 'YOUR_API_KEY'

def get_weather(city):
    cache_data = load_cache()

    if city in cache_data:
        weather_data = cache_data[city]
        if is_cache_valid(weather_data):
            print(f"Weather in {city} (from cache):")
            print_weather_details(weather_data)
            plot_temperature_trend(weather_data)
            return 

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    

    if data["cod"] == "404":
        print(f"City '{city}' not found. Please check the spelling.")
        return

    if data["cod"] == "401":
        print(f"API Key is not working. Try again later.")
        return

    weather_data = extract_weather_data(data)
    cache_data[city] = weather_data
    save_cache(cache_data)
    print("\n")
    capitalized = city.capitalize()
    print(f"{capitalized}'s Weather Tale Unfolds... \n")
    print_weather_details(weather_data)
    plot_temperature_trend(weather_data)
    
    return 

def extract_weather_data(data):
    weather_list = data["list"]
    weather_data = []

    total_items = len(weather_list)
    print("\n")
    with tqdm(total=total_items, desc="Unveiling weather's essence through code's wizardry...", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt} {postfix}", unit="item", ncols=80) as pbar:
        for forecast in weather_list:
            temperature = forecast["main"]["temp"]
            date = forecast["dt_txt"]
            weather_data.append({"date": date, "temperature": temperature})
            pbar.update(1)
            time.sleep(0.1)  # Simulating delay

    return weather_data

def is_cache_valid(weather_data):
    last_updated = datetime.datetime.strptime(weather_data[0]["date"], "%Y-%m-%d %H:%M:%S")
    current_time = datetime.datetime.now()
    time_difference = current_time - last_updated
    return time_difference.total_seconds() <= 3600  # Cache is valid for 1 hour
