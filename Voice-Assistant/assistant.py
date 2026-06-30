import webbrowser
import subprocess

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
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")


def open_google():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")


def open_github():
    speak("Opening GitHub")
    webbrowser.open("https://github.com")

def open_firefox():
    if launch_application("firefox", "Firefox"):
        speak("Opening Firefox")
    else:
        speak("Firefox is not installed.")


def open_vscode():
    speak("Opening Visual Studio Code")
    subprocess.Popen(["code"])


def open_terminal():
    speak("Opening Terminal")
    subprocess.Popen(["konsole"])


def open_files():
    speak("Opening File Manager")
    subprocess.Popen(["dolphin"])

def process_command(command):
    """
    Process user commands.
    Returns False if the assistant should exit.
    """

    if not command:
        speak("I didn't hear anything.")
        return True

    if command == "timeout":
        speak("I didn't hear anything. Please try again.")
        return True

    if command == "unknown":
        speak("Sorry, I couldn't understand what you said.")
        return True

    if command == "error":
        speak("There was a problem connecting to the speech recognition service.")
        return True

    if any(word in command for word in ["hello", "hi", "hey"]):
        greet()

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif command.startswith("search"):
        query = command.replace("search", "", 1).strip()
        search_google(query)

    elif "open youtube" in command:
        open_youtube()

    elif "open google" in command:
        open_google()

    elif "open github" in command:
        open_github()
    elif "open firefox" in command:
        open_firefox()
    elif "open code" in command or "open visual studio code" in command:
        open_vscode()
    
    elif "open terminal" in command:
        open_terminal()
    
    elif "open files" in command or "open file manager" in command:
        open_files()

    elif any(word in command for word in ["exit", "quit", "bye"]):
        speak("Goodbye! Have a great day.")
        return False

    else:
        speak("Sorry, I don't know how to do that yet.")
    

    return True