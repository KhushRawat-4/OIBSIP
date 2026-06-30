import asyncio
import edge_tts
import uuid
import os
import subprocess
import speech_recognition as sr

VOICE = "en-US-AriaNeural"


def speak(text):
    print(f"Assistant: {text}")

    filename = f"speech_{uuid.uuid4().hex}.mp3"

    async def generate():
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save(filename)

    asyncio.run(generate())

    subprocess.run(["mpg123", filename],
                   stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)

    if os.path.exists(filename):
        os.remove(filename)


def listen():
    """
    Listen to user voice and convert it to text.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for background noise
        recognizer.dynamic_energy_threshold = True
        recognizer.pause_threshold = 1.0
        recognizer.non_speaking_duration = 0.5

        recognizer.adjust_for_ambient_noise(source, duration=2)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            command = recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            print(f"You: {command}")

            return command.lower()

        except sr.WaitTimeoutError:
            return "timeout"

        except sr.UnknownValueError:
            return "unknown"

        except sr.RequestError:
            return "error"