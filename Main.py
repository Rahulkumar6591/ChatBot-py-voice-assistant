import pyttsx3 as p
import speech_recognition as sr
from selenium_web import Infow  # Import the Infow class
import time
from YT_auto import *
from news import *
import randfacts
from jokes import *
from Weather import *
import datetime


engin = p.init()
rate = engin.getProperty("rate")
engin.setProperty("rate", 180)
voices = engin.getProperty("voices")
engin.setProperty('voice', voices[0].id)

def speak(text):
    engin.say(text)
    engin.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return ("Morning")
    elif hour>=12 and hour<16:
        return ("afternoon")
    else:
        return ("Evening")

today_date=datetime.datetime.now()

r = sr.Recognizer()

speak("hello sir, good "+wishme()+", I'm your voice assistant.")
speak("Today is " + today_date.strftime("%d") + 
      " of " + today_date.strftime("%B") + 
      ", and it's currently " + today_date.strftime("%I:%M %p") + ".")
speak("Temperature in bodhgaya is " +str(temp())+"degree celcius " + "and with "+str(des()))

speak("What can I do for you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" in text and "about" in text and "you" in text:
    speak("I am also having a good day, sir")
# speak("What can I do for you?")

with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source, 1.2)
    print("Listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "i need information" in text2:
    speak("You need information related to which topic?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)

    speak(f"Searching {infor} in Wikipedia.")
    assist = Infow()  # Create an instance of Infow
    assist.get_info(infor)
    time.sleep(10)

elif "play" and "video" in text2:
    speak("You want to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    
    print("Playing {} on YouTube".format(vid))
    assist = Music()  # Correct class name with uppercase "M"
    assist.play(vid)

elif "news" in text2:
    print("Sure sir, Now I will read some news for you.")
    speak("Sure sir, Now I will read some news for you.")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])


# elif "fact" or "facts" in text2:
#     speak("Sure sir, ")
#     x=randfacts.getFact()
#     print(x)
#     speak("Did you know that, "+x)


elif "joke" in text2:
    speak("Sure sir, get ready for some chuckles")
    arr = joke()  # Call the joke function
    print(arr[0])  # Print the joke setup
    speak(arr[0])  # Speak the joke setup
    #time.sleep(1)  # Pause to let the setup finish
    print(arr[1])  # Print the punchline
    speak(arr[1])  # Speak the punchline