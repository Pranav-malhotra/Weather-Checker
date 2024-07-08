import os
import json

CACHE_FILE = "weather_cache.json"

def load_cache():
    if not os.path.isfile(CACHE_FILE):
        return {}
    with open(CACHE_FILE, "r") as file:
        try:
            cache_data = json.load(file)
        except json.JSONDecodeError:
            cache_data = {}
    return cache_data

def save_cache(cache_data):
    with open(CACHE_FILE, "w") as file:
        json.dump(cache_data, file, indent=4)
