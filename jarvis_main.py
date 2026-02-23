import os
import webbrowser
import datetime
import pyautogui
from openai import OpenAI

from wake_word import wait_for_wake_word
from listener import listen
from tts import speak
from gui import JarvisGUI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

gui = JarvisGUI()

def authenticate():
    return True

def jarvis_brain():
    while True:
        command = listen(timeout=8, phrase_time_limit=8)

        if command == "":
            speak("Going back to sleep.")
            break

        if "exit" in command or "stop" in command:
            speak("Goodbye.")
            exit()

        if "open chrome" in command:
            speak("Opening Chrome")
            os.system("start chrome")
            continue

        if "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
            continue

        if "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")
            continue

        speak("Thinking")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": command}]
        )
        speak(response.choices[0].message.content.strip())

def main():
    speak("Jarvis online")
    while True:
        gui.set_status("SLEEP")
        wait_for_wake_word()

        gui.set_status("ACTIVE")
speak("Access granted")
jarvis_brain()
    
if __name__ == "__main__":
    main()
