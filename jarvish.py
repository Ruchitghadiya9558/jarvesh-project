import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good after noon!")
    else:
        speak("Good evening!")

    speak("i am ruchit sir. pleace tell me how may i help you")

def tackecommand():
    # it tacke microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)

        print("say  that again please....")
        return "none"
    return query


if __name__ == "__main__":
    wishme()

    while True:
        query = tackecommand().lower()
        # speak("ruchit  is a good boy")
        if 'wikipedia' in query:
                speak("searching wikipedia....")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=3)
                speak("according to wikipedia")
                print(result)
                speak(result)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open Qmamu" in query:
            webbrowser.open("qmamu.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")

        elif "open instagram" in query:
            webbrowser.open("instagram.com")

        elif "open whatsapp" in query:
            webbrowser.open("whatsapp.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif "open code" in query:
            codepath = "C:\Program Files (x86)\Sublime Text 3\sublime_text.exe"
            os.startfile(codepath)

        elif "play music" in query:
            music_dir = "D:\mp3\mp3\Shree Ram Audio"
            songs = os. listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))




