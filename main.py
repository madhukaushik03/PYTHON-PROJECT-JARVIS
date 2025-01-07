import speech_recognition as sr
import webbrowser
import pyttsx3 #text-to-speech

# recogniser = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text) 
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    if "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    if "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    if "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    if "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    if "close google" in c.lower():
        pass

    

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    
    while True:
        #listen for the wake word- Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        # recognize 
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            # print(word) 
            if(word.lower() == "jarvis"):
                speak("yeah")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print(f"error; {e}")
