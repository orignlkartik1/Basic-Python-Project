import pyttsx3 as py
import datetime as dt
import wikipedia as wiki
import webbrowser as wb
import pyjokes as pj


def speak(text):
    print(f"Assistant: {text}")
    try:
        engine = py.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id) # you can change this voice.{'0':"boy","1":"girl"}
        engine.say(text)
        engine.runAndWait()
    except:
        print("Speech output not supported in Colab.")


def greet():
    hour = int(dt.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your voice assistant. How can I help you today?")

def take():
    return input("You (type your command): ").lower()

def run():
    greet()
    while True:
        query = take()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wiki.summary(query, sentences=2)
                speak("According to Wikipedia:")
                speak(result)
            except:
                speak("Sorry, I couldn't find anything.")

        elif 'open youtube' in query:
            speak("Opening YouTube...")
            wb.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Opening Google...")
            wb.open("https://www.google.com/")

        elif 'time' in query:
            strTime = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {strTime}")

        elif 'joke' in query:
            joke = pj.get_joke()
            speak(joke)

        elif "learn" in query:
            speak("learn anything.......")
            wb.open('https://learn-anything.xyz/')

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a nice day!")
            break

        else:
            speak("Sorry, I didn't understand that. Try again.")

run()
