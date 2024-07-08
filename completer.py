import requests
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion

class CityNameCompleter(Completer):
    def get_completions(self, document, complete_event):
        city_prefix = document.text_before_cursor
        if city_prefix:
            url = f"http://api.geonames.org/searchJSON?q={city_prefix}&maxRows=10&username=nandinigera18"
            response = requests.get(url)
            data = response.json()
            if "status" in data:
                print(data["status"]["message"])
            suggestions = [item["name"] for item in data["geonames"]]
            for suggestion in suggestions:
                yield Completion(suggestion, start_position=-len(city_prefix), display_meta="City")


