import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Configure voice properties
engine.setProperty("rate", 170)      # Speaking speed
engine.setProperty("volume", 1.0)    # Volume (0.0 to 1.0)


def speak(text):
    """
    Convert text to speech.
    """
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    """
    Listen to the user's voice and convert it to text.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio = recognizer.listen(source, timeout=5)

            command = recognizer.recognize_google(audio)

            print(f"You: {command}")

            return command.lower()

        except sr.WaitTimeoutError:
            return "timeout"

        except sr.UnknownValueError:
            return "unknown"

        except sr.RequestError:
            return "error"