import pystray
from PIL import Image
from datetime import datetime, timedelta
import threading
from compare_weather import get_weather_data
import platform
from plyer import notification
import schedule
import time

interval_weather = []  # Define the interval_weather array globally


class UpdateInfoMenuItem(pystray.MenuItem):
    def __init__(self, default_location):
        self.default_location = default_location
        self.weather_data = get_weather_data(default_location)
        self.last_updated_time = datetime.now()  # Initialize last_updated_time to None
        self.update_frequency = None  # Default update frequency is 10 minutes
        self.update_timer = None  # Initialize the update timer to None
        super().__init__('Update Info', self.update_weather)
        self.start_update_timer()  # Start the timer initially

    def set_update_frequency(self, frequency):
        self.update_frequency = frequency
        print("Update frequency set to: ", self.update_frequency)
        self.start_update_timer()

    def start_update_timer(self):
        if self.update_timer:
            self.update_timer.cancel()
        if self.update_frequency:
            self.update_timer = threading.Timer(self.update_frequency * 60, self.update_weather)
            self.update_timer.start()

    def update_weather(self):
        self.weather_data = get_weather_data(self.default_location)
        formatted_weather_data = self.format_data()
        print("Time Interval in minutes:", self.update_frequency)
        print("Most Recent Weather Data:", formatted_weather_data)
        if platform.system() == 'Windows':
            notification_title = "Your Weather Update:"
            notification_message = formatted_weather_data
            notification.notify(title=notification_title, message=notification_message, timeout=10)
        self.start_update_timer()

    def format_data(self):
        count = 0
        global interval_weather  # Access the globally defined interval_weather array
        interval_weather = []  # Clear the array before updating
        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        tomorrow = today + timedelta(days=1)
        for entry in self.weather_data:
            dt_str = entry["date"]
            temperature = entry["temperature"]

            dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
            if dt.date() == today.date():
                dt_formatted = dt.strftime('%I:%M %p')
            elif dt.date() == tomorrow.date():
                dt_formatted = f"Tom, {dt.strftime('%I:%M %p')}"

            temperature_celsius = round(temperature - 273, 1)

            interval_weather.append(f"{dt_formatted}: {temperature_celsius}°C")

            count += 1
            if count == 3:
                break

        formatted_time = now.strftime('%H:%M')

        return "Last Updated: " + formatted_time + " | " + " | ".join(interval_weather)

    
    def data_array(self):
        global interval_weather  # Access the globally defined interval_weather array
        return interval_weather

    @property
    def text(self):
        return self.format_data()


def exit_action(icon, item):
    icon.stop()


def create_icon(default_location):
    image = Image.open("weather.png")
    update_menu_item = UpdateInfoMenuItem(default_location)

    def set_update_frequency_10(item):
        update_menu_item.set_update_frequency(10)
        

    def set_update_frequency_15(item):
        update_menu_item.set_update_frequency(15)


    def set_update_frequency_30(item):
        update_menu_item.set_update_frequency(30)

    def set_update_frequency_60(item):
        update_menu_item.set_update_frequency(60)


    def set_update_frequency_none(item):
        update_menu_item.set_update_frequency(None)

    def empty(item):
        return default_location

    submenu = pystray.Menu(
        pystray.MenuItem('Every 10 mins', set_update_frequency_10),
        pystray.MenuItem('Every 15 mins', set_update_frequency_15),
        pystray.MenuItem('Every 30 mins', set_update_frequency_30),
        pystray.MenuItem('Every 1 hour', set_update_frequency_60),
        pystray.MenuItem('Turn Off', set_update_frequency_none),
    )
        
    menu = (
        update_menu_item,
        pystray.MenuItem('Enable Automatic Notifications', submenu),
        pystray.MenuItem(f'Default Location: {default_location}', empty, enabled=False),
        pystray.MenuItem('Exit', exit_action),
    )

    icon = pystray.Icon("Drizzle_Systray_Icon", image, "Drizzle", menu)
    icon.menu = menu

    return icon


def system_tray(default_location):
    icon = create_icon(default_location)

    try:
        icon.run()
    except AttributeError as e:
        print(f"Error: {e} - Please check if the required methods exist in the pystray library.")

