import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import sys
import time
import webbrowser

# Initialize recognizer and TTS engine once
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set your microphone index (from your mic list)
MIC_DEVICE_INDEX = 1  # Microphone (Realtek Audio)

# Text-to-Speech function
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to get voice input
def input_instruction():
    try:
        with sr.Microphone(device_index=MIC_DEVICE_INDEX) as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source, duration=1)
            audio = listener.listen(source, phrase_time_limit=8)
            print("Processing speech...")
            instruction = listener.recognize_google(audio).lower()
            print("Recognized:", instruction)  # Debug
            return instruction
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Speech Recognition service error:", e)
    except Exception as e:
        print("Error:", e)
    return ""

# Main assistant loop
def play_pratham():
    while True:
        instruction = input_instruction()

        if instruction == "":
            time.sleep(1)
            continue

        print("You said:", instruction)

        # Play any song/video on YouTube
        if "play" in instruction:
            song = instruction.replace("play", "").strip()
            talk("Playing " + song)
            pywhatkit.playonyt(song)

        # Open YouTube homepage
        elif "open youtube" in instruction:
            talk("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        # Open YouTube Shorts
        elif "open youtube shorts" in instruction:
            talk("Opening YouTube Shorts")
            webbrowser.open("https://www.youtube.com/shorts")

        # Tell current time
        elif "time" in instruction:
            time_now = datetime.datetime.now().strftime('%I:%M %p')
            talk("Current time is " + time_now)

        # Tell current date
        elif "date" in instruction:
            date_today = datetime.datetime.now().strftime('%d/%m/%Y')
            talk("Today's date is " + date_today)

        # Basic conversation
        elif "how are you" in instruction:
            talk("I am fine, how about you")

        elif "what is your name" in instruction:
            talk("I am Pratham, your virtual assistant")

        # Wikipedia search
        elif "who is" in instruction:
            human = instruction.replace("who is", "").strip()
            try:
                info = wikipedia.summary(human, sentences=2)
                print(info)
                talk(info)
            except Exception as e:
                talk("Sorry, I could not find information on " + human)

        # Exit assistant
        elif "exit" in instruction or "stop" in instruction:
            talk("Goodbye!")
            sys.exit(0)

# Run the assistant
play_pratham()
