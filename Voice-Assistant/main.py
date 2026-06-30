from speech import speak, listen
from assistant import process_command

def main():
    speak("hello! I am your Voice Assistant")

    running = True
    while running:
        command = listen()
        running = process_command(command)

if __name__ == "__main__":
    main()