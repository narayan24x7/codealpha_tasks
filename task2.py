import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit as kit
import wikipedia
import os

# Initialize the recognizer and the TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function for text-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to get the current date and time
def tell_time():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    speak(f"The current time is {time}")

def tell_date():
    now = datetime.datetime.now()
    date = now.strftime("%B %d, %Y")
    speak(f"Today is {date}")

# Function to search on Wikipedia
def search_wikipedia(query):
    speak(f"Searching Wikipedia for {query}")
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results, please be more specific.")
    except wikipedia.exceptions.HTTPTimeoutError:
        speak("Sorry, I'm having trouble accessing Wikipedia right now.")
    except Exception as e:
        speak("Sorry, I couldn't find anything on Wikipedia.")

# Function to play a YouTube video
def play_on_youtube(query):
    speak(f"Playing {query} on YouTube")
    kit.playonyt(query)

# Function to take voice input from the user
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print(f"You said: {command}")
            return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble connecting to the speech recognition service.")
        return ""

# Main function
def main():
    speak("Hello, I am your voice assistant. How can I help you?")
    
    while True:
        command = take_command()

        if 'time' in command:
            tell_time()
        elif 'date' in command:
            tell_date()
        elif 'search' in command or 'wikipedia' in command:
            query = command.replace("search", "").replace("wikipedia", "").strip()
            search_wikipedia(query)
        elif 'play' in command:
            song = command.replace("play", "").strip()
            play_on_youtube(song)
        elif 'open' in command:
            app = command.replace("open", "").strip()
            speak(f"Opening {app}")
            os.system(f"start {app}")  # Works on Windows, adjust for macOS/Linux
        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    main()
