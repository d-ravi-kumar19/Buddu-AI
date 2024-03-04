import os
import pyttsx3
import subprocess
import webbrowser
import datetime
import json

def speak(text, rate=160, voice_id='com.apple.speech.synthesis.voice.fiona'):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('voice', voice_id)
    engine.say(text)
    engine.runAndWait()

def open_application(target):
    try:
        subprocess.Popen([target])
        speak(f"{target} opened.")
    except Exception as e:
        speak(f"Error opening {target}: {str(e)}")

def search_in_browser():
    query = input("Enter your search query: ")
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    speak(f"Searching Google for: {query}")

def tell_date_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    speak(f"The current time is {current_time} and the date is {current_date}.")

if __name__ == "__main__":
    speak("Hello! How can I assist you today?")

    with open("commands_config.json", "r") as config_file:
        commands_config = json.load(config_file)

    while True:
        user_input = input("Enter your command: ").lower()

        if user_input == "exit":
            speak("Goodbye!")
            break

        if user_input in commands_config["commands"]:
            command_info = commands_config["commands"][user_input]
            action = command_info["action"]
            target = command_info["target"]

            if action == "open":
                open_application(target)
            elif action == "close":
                subprocess.Popen(["taskkill", "/f", "/im", target])
            elif action == "search_browser":
                search_in_browser()
            elif action == "tell_date_time":
                tell_date_time()
            else:
                speak("Unsupported action in command configuration.")
        else:
            print("Command not recognized. Please try again.")
