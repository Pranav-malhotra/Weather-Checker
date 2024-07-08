def print_weather_details(weather_data):
    print("{:<12} {:<12} {:<10}".format("Date", "Time", "Temperature (°C)", "Color"))
    for forecast in weather_data:
        date_and_time_Array = forecast["date"].split()
        date = date_and_time_Array[0]
        time = date_and_time_Array[1]
        temperature_k = forecast["temperature"]
        temperature_c = temperature_k - 273.15
        color = get_temperature_color(temperature_c)
        formatted_temperature = format_temperature_with_color(temperature_c, color)
        print("{:<12} {:<12} {:<18}".format(date, time, formatted_temperature))

def get_temperature_color(temperature):
    # Define color ranges and corresponding values
    color_ranges = [(0, 5), (5, 10), (10, 15), (15, 25), (25, 32), (32, 36), (36, float("inf"))]
    color_values = ['\033[94m', '\033[96m', '\033[36m', '\033[92m', '\033[93m', '\033[91m', '\033[31m']

    # Find the color corresponding to the temperature
    for i, (min_temp, max_temp) in enumerate(color_ranges):
        if min_temp <= temperature < max_temp:
            return color_values[i]

    return '\033[30m'  # Default color if temperature falls outside the defined ranges

def format_temperature_with_color(temperature, color):
    return f"{color}{temperature:.2f} °C\033[0m"
