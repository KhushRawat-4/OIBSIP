from commands import get_weather
from speech import speak
from commands import (
    greet,
    tell_time,
    tell_date,
    search_google,
    open_youtube,
    open_google,
    open_github,
    open_firefox,
    open_vscode,
    open_terminal,
    open_files,
)

def process_command(command):
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
    
    elif "weather" in command:
        if "in" in command:
            city = command.split("in", 1)[1].strip()
            if city:
                get_weather(city)
        else:
            get_weather()

    elif any(word in command for word in ["exit", "quit", "bye"]):
        speak("Goodbye! Have a great day.")
        return False

    else:
        speak("Sorry, I don't know how to do that yet.")

    return True