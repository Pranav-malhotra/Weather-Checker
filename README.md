# Drizzle
## Command-Line Weather Forecast Tool

This command-line tool lets you fetch a specific city's current weather forecast using the OpenWeatherMap API. It also incorporates data visualization capabilities to present weather data visually appealingly.

# Table of Contents
1. [Features](#features)
2. [Use of GitHub Copilot and Microsoft Technologies](#use-of-github-copilot-and-microsoft-technologies)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Customization](#customization)
7. [Acknowledgments](#acknowledgments)
8. [Screenshots](#screenshots)


## Features

- **Real-time Weather Forecast** :partly_sunny: : Fetches the current weather forecast for a specified city, keeping you up-to-date with the latest conditions.

- **Powered by OpenWeatherMap API** :earth_americas: : Utilizes the reliable and accurate OpenWeatherMap API to retrieve precise weather data.

- **Data Extraction and Parsing** :mag_right: : Automatically extracts and parses the API response to extract relevant weather information, providing you with concise and meaningful data.

- **Robust Error Handling** :warning: : Implements robust error handling for API requests and responses. Seamlessly handles misspelled city names and displays informative error messages.

- **Stunning Data Visualization** :bar_chart: : Experience weather patterns and trends come to life through visually appealing charts powered by Matplotlib. Explore the data with interactive and downloadable graphs.

- **Personalized Interaction** :bust_in_silhouette: : Enjoy an interactive and personalized experience. The tool greets you by name and prompts further actions through intuitive commands.

- **Flexible Location Options** :round_pushpin: : Choose between using a default location or inputting a new one, giving you the flexibility to explore weather forecasts for any desired location.

- **Detailed Forecast Display** :calendar: : Get a comprehensive view of the weather forecast for the next six days at various intervals, ensuring you have all the information you need to plan ahead.

- **Convenient Default Location** :house_with_garden: : Set your previously entered location as the default for subsequent runs, saving you time and effort.

- **Caching Weather Data** :floppy_disk: : Implements caching of weather data to improve performance and reduce API calls. The tool checks the cache for previously fetched weather data for a specific city and retrieves it if available, saving time and resources.

- **Notifications**: :bell: Receive timely notifications about weather updates and alerts. The tool sends notifications based on changes in weather conditions, ensuring you stay informed about important weather events.

Enhance your weather exploration with this feature-rich tool. Read about the features in detail. 😎🌦️

## Use of GitHub Copilot and Microsoft Technologies 

| Feature | Description | Implementation with **GitHub Copilot** and **Microsoft Technologies** | User Benefits | Tech Stack Used |
| --- | --- | --- | --- | --- |
| **Graphs** | Visualize weather data trends with interactive charts | Utilized GitHub Copilot to assist in generating code for chart rendering and data visualization. Enhanced the visualization of the graph using suggestions made by GitHub Copilot. | Easily track and analyze historical weather patterns and forecast trends. <br> Make informed decisions based on visual insights. | GitHub Copilot, <br> Data Analytics, <br> MATPLOTLIB library |
| **Autocomplete** | Start typing a city name and get suggestions to complete it. | Integrated GitHub Copilot to optimize the autocomplete feature and used GeoNames API to fetch city names for the suggestions. | Save time and avoid typos by quickly selecting the correct city name from the suggested options. The suggestions are retrieved from the GeoNames API, ensuring that valid and up-to-date city names are provided.| GitHub Copilot, <br> GeoNames API, <br> prompt_toolkit, prompt, prompt_toolkit.completion, <br> Completer, and Completion libraries. |
| **Cache Management** | The cache mechanism implemented in the code allows for quicker retrieval of weather data for previously searched cities, reducing response times and minimizing dependence on external APIs | Utilized GitHub Copilot to assist in implementing cache management functionality. | Faster retrieval of weather data, reduced API calls, and improved overall performance. | GitHub Copilot |
| **Interactive Mode** | Engage with real-time weather information through command-line controls | Leveraged GitHub Copilot's code generation capabilities to build interactive controls. Utilized the capabilities of GitHub Copilot to generate test cases and identify errors automatically. | Explore current weather conditions, forecasts, and additional details interactively. Interactive mode simplifies the input process for users by presenting them with clear choices and prompts. This reduces the chances of input errors and ensures that users provide the required information in a structured and consistent manner. | GitHub Copilot, <br> JSON library (for configuration file handling), <br> PIL (Python Imaging Library, for working with images) |                 
| **Compare Weather** | Compare weather conditions between multiple locations side by side | Employed GitHub Copilot to assist in developing the comparison feature, enabling simultaneous display of weather data for different locations. <br> Used Data Analytics to compare weather between two cities and display the comparison through a graph, each city with a different color, making it easy for the user to conclude decisions. | Plan trips, events, or outdoor activities by comparing weather forecasts for different locations. Make well-informed decisions based on comprehensive weather comparisons. | GitHub Copilot, <br> OpenWeather API, <br> Data Analytics, <br> REQUESTS library (for making API requests), <br> MATPLOTLIB library |
| **System Tray Icon** | Access weather information directly from the system tray | Utilized GitHub Copilot's code generation capabilities to implement system tray functionality, enabling users to easily access weather information with a single click. Interact with the application without the need for a separate window. | Check current weather conditions and temperature, or receive notifications without opening the app. Conveniently stay informed with just a glance. | GitHub Copilot, <br> PYSTRAY library |
| **Auto Update in Background** | Automatically fetch updated weather data at regular intervals. The tool continuously retrieves the latest weather data at predefined intervals and informs the user about current weather conditions. | Utilized GitHub Copilot's code suggestions to develop the background auto-update functionality. This ensures users can access the latest and most accurate weather information without manual intervention. Integrated Microsoft technologies to display notifications with updated weather information. | Stay up-to-date with the latest weather information without manual intervention. Ensure accurate and timely forecasts without needing to refresh or manually update constantly. | GitHub Copilot, <br> SCHEDULE library |
| **Notifications** | Automatically fetch updated weather data at regular intervals | Integrated GitHub Copilot's generated code with Microsoft technologies for enhanced functionality and seamless user experience. Utilised Microsoft technologies to display notifications with updated weather information. | Remain informed about weather changes throughout the day, ensuring preparedness for outdoor activities or travel plans. Receive notifications on your desktop, ensuring you don't miss any critical weather information. | GitHub Copilot, <br> PLYER library, <br> SCHEDULE library |
| **Personalization** | Customize app settings, preferences, and the default location. | Employed GitHub Copilot to streamline the development of personalization features, allowing users to customize various app settings. | Tailor the app to suit individual preferences with various options such as using the default location to fetch weather, auto-update the same in the background or even enter a new city and compare weather. Enhances the user experience and creates a personalized weather app environment. | GitHub Copilot |


Prerequisites
-------------

Before running the tool, make sure you have the following prerequisites installed:

*   Python (version 3.10 or higher)
*   pip (to install Python packages)
    

Installation
------------

1.  Clone the repository or download the source code files.
    
2.  Open a terminal or command prompt and navigate to the project directory.
    
3.  Install the required Python dependencies by running the following command:
    
    `pip install -r requirements.txt`
 
Generate API Keys
-----------------
1. Go to the OpenWeather website (https://openweathermap.org/) and create an account if you don't have one already.
2. Once logged in, go to the "API Keys" section in your account dashboard.
3. Click on the "Create Key" button to generate a new API key.
4. Give your API key a name and select the desired access level (e.g., "Free" or "Paid").
5. Copy the generated API key to your clipboard.
6. Open the weather.py file in your preferred text editor.
7. Find the placeholder for the API key in the code (e.g., `API_KEY = "<YOUR_API_KEY>"`).
   
   ![image](https://github.com/vatsal-dev/Drizzle/assets/61816778/53050a9f-060c-4c11-b630-e940e9a1c341)

9. Replace `<YOUR_API_KEY>` with the API key you copied in Step 5.
10. Save the weather.py file.
11. You are now ready to use the OpenWeather API with your generated API key in the weather.py script.


Usage
-----

To use the Weather App, follow these steps:

1.  Open a terminal or command prompt and navigate to the project directory.
    
2.  Run the `main.py` file using the following command:
    
    
    ```cli
    python main.py
    ```
    
3.  The app will prompt you to enter your name and choose an option:
    
    ```sql
    Hey [Your Name]. Welcome back! Choose an option:
    
    1. Use default location
    2. Open default location in system tray
    3. Use a new location
    4. Compare weather of two locations
    
    Enter your choice (1, 2, 3, or 4):
    ```
    
4.  Enter the corresponding number for the desired option and follow the prompts:
    
    *   Option 1: Use the default location
        
        *   The app will retrieve the weather information for the default location.
        *   The weather details will be displayed in the terminal.
    *   Option 2: Open the default location in the system tray
        
        *   The app will open the default location's weather information in the system tray.
        *   A system tray icon will display weather details upon interaction.
    *   Option 3: Use a new location
        
        *   Enter the new location for which you want to retrieve the weather information.
        *   The weather details will be displayed in the terminal.
    *   Option 4: Compare the weather of two locations
        
        *   Enter the names of the two cities you want to compare.
        *   The app will retrieve the weather data for both cities and display a comparison.
5.  After choosing an option, the app will store your name and selected location in a configuration file (`config.json`) for future use.
    
6.  You can rerun the app to perform additional actions or update your preferences.
    

Customization
-------------

*   Default Location: The default location is set in the `CONFIG_FILE` variable in the `main.py` file. You can modify the value to your desired default location.
    
*   Weather API: The Weather App uses external APIs to fetch weather data. The `weather.py` module contains the `get_weather` function, which can be modified to use a different weather API if needed.

![image](https://github.com/vatsal-dev/Drizzle/assets/61816778/429041ff-c566-4588-b883-53cfe8f46041)


    
Acknowledgments
----------------

The Weather App makes use of the following open-source libraries:

*   PyStray: [https://github.com/moses-palmer/pystray](https://github.com/moses-palmer/pystray)
*   Pillow (Python Imaging Library): [https://python-pillow.org/](https://python-pillow.org/)
*   Prompt Toolkit: [https://python-prompt-toolkit.readthedocs.io/](https://python-prompt-toolkit.readthedocs.io/)
    
Screenshots
-----------

[Google Drive Link to View Screenshots](https://drive.google.com/file/d/1Z-JRecsJBLYZ82tb2Pl-J6nsS_4PKBiN/view?usp=sharing)

      

Thank You!
