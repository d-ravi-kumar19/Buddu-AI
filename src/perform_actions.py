import json
import subprocess
import webbrowser
import pyttsx3
import datetime
import os

def speak(text, rate=160, voice_id='com.apple.speech.synthesis.voice.fiona'):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('voice', voice_id)
    engine.say(text)
    engine.runAndWait()

def execute_command(command_info):
    action = command_info["action"]
    target = command_info["target"]

    if action == "open":
        try:
            app_name = os.path.basename(target).replace(".exe", "")
            subprocess.Popen([target])
            speak(f"{app_name} opened.")
        except Exception as e:
            speak(f"Error opening {app_name}: {str(e)}")


def load_commands_config():
    with open("commands_config.json", "r") as config_file:
        return json.load(config_file)

if __name__ == "__main__":
    speak("Performing actions based on commands configuration.")

    commands_config = load_commands_config()

    while True:
        user_input = input("Enter your command: ").lower()

        if user_input == "exit":
            speak("Goodbye!")
            break

        if user_input in commands_config["commands"]:
            command_info = commands_config["commands"][user_input]
            execute_command(command_info)
        else:
            print("Command not recognized. Please try again.")
