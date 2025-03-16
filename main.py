import speech_recognition as sr
import webbrowser
import pyttsx3 #text-to-speech
import musicLibrary
import requests
import wikipedia  # For Wikipedia search
import sympy as sp # For solving mathematical equations


# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed (words per minute)
engine.setProperty('volume', 1.0)  # Volume level between 0.0 and 1.0
# apikey = "bedd6e9ac06c4e0285327a36efe76f1c" #api key


# Speak function
def speak(text):
    engine.say(text) 
    engine.runAndWait()

# Process Command Function
def processCommand(c):
    if "help" in c.lower():
        help_text = """
        I can perform the following tasks:
         I Open websites like Google, YouTube, Facebook, Instagram, LinkedIn, and ChatGPT.
         I Play your favorite songs.
         I Fetch the latest news headlines.
         I Perform math calculations. Just say "solve" followed by your equation.
         I Search Wikipedia for any topic. Just say "search" followed by the topic.
        """
        speak(help_text)
        print(help_text)
    elif "solve" in c.lower():
        try:
            equation = c.lower().replace("solve", "").strip()
            result = sp.sympify(equation)
            speak(f"The result of {equation} is {result}")
            print(f"The result of {equation} is {result}")
        except Exception as e:
            speak("I couldn't solve that equation. Please try again.")
            print(f"Error solving equation: {e}")
    # elif "search" in c.lower():
    #     try:
    #         query = c.lower().replace("search", "").strip()
    #         summary = wikipedia.summary(query, sentences=2)
    #         speak(f"Here is what I found about {query}: {summary}")
    #         print(f"Wikipedia Summary: {summary}")
    #     except wikipedia.exceptions.DisambiguationError as e:
    #         speak("Your search term is ambiguous. Please provide more specific keywords.")
    #         print(f"Disambiguation Error: {e}")
    #     except Exception as e:
    #         speak("I couldn't find any information on that topic.")
    #         print(f"Error searching Wikipedia: {e}")

    elif "search" in c.lower():
        try:
            # Extract query from the command
            query = c.lower().replace("search", "").strip()
            # Format query for proper capitalization
            query = query.title()
            print(f"Searching Wikipedia for: {query}")

            # Fetch summary from Wikipedia
            summary = wikipedia.summary(query, sentences=2)
            speak(f"Here is what I found about {query}: {summary}")
            print(f"Wikipedia Summary: {summary}")
        except wikipedia.exceptions.DisambiguationError as e:
            speak(f"Your search term is ambiguous. Please provide more specific keywords.")
            print(f"Disambiguation Error: {e.options}")
        except wikipedia.exceptions.PageError:
            speak(f"I couldn't find any information on {query}. Please try a different search term.")
            print(f"PageError: No Wikipedia page for '{query}'")
        except Exception as e:
            speak("An error occurred while searching Wikipedia. Please try again.")
            print(f"Error in search: {e}")

    elif "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://www.chatgpt.com/")
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
    # else: intergration with openAI and let openai handle the request pass

    else:
        speak("I'm sorry, I didn't understand that command.")
        print("Unrecognized command.")



   

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
