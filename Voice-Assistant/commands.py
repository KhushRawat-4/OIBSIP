import webbrowser
import requests
from config import WEATHER_API_KEY, DEFAULT_CITY
from speech import speak
from utils import get_current_time, get_current_date
from utils import launch_application

def greet():
    speak("Hello! How can I help you today?")


def tell_time():
    speak(f"The current time is {get_current_time()}")


def tell_date():
    speak(f"Today is {get_current_date()}")


def search_google(query):
    if query:
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    else:
        speak("Please tell me what you want to search.")


def open_youtube():
    speak("Opening Youtube")
    webbrowser.open("https://www.youtube.com")

def open_google():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")



def open_github():
    speak("Opening GitHub")
    webbrowser.open("https://www.github.com")


def open_firefox():
    if launch_application("firefox", "Firefox"):
        speak("Opening Firefox")
    else:
        speak("Firefox is not installed.")


def open_vscode():
    if launch_application("code", "Visual Studio Code"):
        speak("Opening Visual Studio Code")
    else:
        speak("Visual Studio Code is not installed.")


def open_terminal():
    if launch_application("konsole", "terminal"):
        speak("Opening terminal")
    else:
        speak("konsole is not installed.")


def open_files():
    if launch_application("dolphin", "File Manager"):
        speak("Opening File Manager")
    else:
        speak("File Manager is not installed.")

def get_weather(city=DEFAULT_CITY):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code !=200:
            speak("sorry, i couldm't fetch the weather.")
            return
        
        city_name = data["name"]
        temp = data["main"]["temp"]
        humidity= data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        speak(
            f"The weather in {city_name} is {condition}. "
            f"Temperature is {temp} degrees celsius "
            f"with {humidity} percent humidity."
        )
    except requests.exception.RequestException:
        speak("Network error while fetching weather.")