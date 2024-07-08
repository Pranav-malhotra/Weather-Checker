import matplotlib.pyplot as plt
import numpy as np

def plot_temperature_trend(weather_data):
    dates_list = [forecast["date"] for forecast in weather_data]
    temperature_list = [forecast["temperature"] - 273.15 for forecast in weather_data]  # Convert from Kelvin to Celsius

    # Create a higher density x-axis for the smooth curve
    x = np.linspace(0, len(dates_list) - 1, 2000)

    plt.figure(figsize=(10, 6))
    plt.plot(x, np.interp(x, range(len(dates_list)), temperature_list), color='blue', linestyle='-', linewidth=2)
    plt.scatter(range(len(dates_list)), temperature_list, color='blue', marker='o')
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Trend")

    tick_positions = range(0, len(dates_list), 2)
    tick_labels = dates_list[::2]
    plt.xticks(tick_positions, tick_labels, rotation=45, fontsize=8)

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


# function used to create plot for comparison of temperature
def plot_temperature_twoInOne(data1, city1, data2, city2):
    dates1 = []
    temperatures1 = []

    for item in data1:
        date = item['date']
        temperature = item['temperature'] - 273.15  # Convert from Kelvin to Celsius
        dates1.append(date)
        temperatures1.append(float(temperature))

    dates2 = []
    temperatures2 = []

    for item in data2:
        date = item['date']
        temperature = item['temperature'] - 273.15  # Convert from Kelvin to Celsius
        dates2.append(date)
        temperatures2.append(float(temperature))

    plt.figure(figsize=(10, 6))  # Adjust the figure size for better readability
    plt.plot(dates1, temperatures1, label=city1, color='red')
    plt.plot(dates2, temperatures2, label=city2, color='blue')

    plt.xlabel("Date and Time")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Comparison")
    plt.legend()  # Add a legend to distinguish between cities

    plt.xticks(rotation=45, ha='right', fontsize=8)  # Rotate and align x-axis ticks for readability

    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()


