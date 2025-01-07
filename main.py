import speech_recognition as sr
import webbrowser
import pyttsx3 #text-to-speech
import musicLibrary
import requests


# recogniser = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed (words per minute)
engine.setProperty('volume', 1.0)  # Volume level between 0.0 and 1.0
apikey = "bedd6e9ac06c4e0285327a36efe76f1c" #api key
# bedd6e9ac06c4e0285327a36efe76f1c
def speak(text):
    engine.say(text) 
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    # elif "close google" in c.lower():
    #     pass
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.favsongs[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=bedd6e9ac06c4e0285327a36efe76f1c")
        # Ensure the request was successful
        if r.status_code == 200:
            # Parse the JSON respose
            data = r.json()
            
            # Extract articles
            articles = data.get('articles', [])
            titles = [article['title'] for article in articles if 'title' in article]
            
            # speak all headlines
            for title in titles:
                speak(title)
        # else:
        #     print(f"Failed to fetch data: {r.status_code}")
    else:
        #intergration with openAI and let openai handle the request
        pass



   

if __name__ == "__main__":
    speak("...Initializing Jarvis")
    
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
