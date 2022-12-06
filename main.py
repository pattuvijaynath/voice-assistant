import speech_recognition as sr
import pyttsx3
import wikipedia
import music
import time
import pytube
import vlc
from youtube_search import YoutubeSearch
import pyjokes
import webbrowser
import cv2
import keyboard
import random

greetings = ["hi", "hello", "hey", "helloo", "hellooo", "g morining", "gmorning", "good morning", "morning", "good day", "good afternoon", "good evening", "greetings", "greeting", "good to see you", "its good seeing you", "how are you", "how're you", "how are you doing", "how ya doin'", "how ya doin", "how is everything", "how is everything going", "how's everything going", "how is you", "how's you", "how are things", "how're things", "how is it going", "how's it going", "how's it goin'", "how's it goin", "how is life been treating you", "how's life been treating you", "how have you been", "how've you been", "what is up", "what's up", "what is cracking", "what's cracking", "what is good", "what's good", "what is happening", "what's happening", "what is new", "what's new", "what is neww", "g’day", "howdy"]


engine = pyttsx3.init()


def speak(words):
    engine.say(words)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")

    return query


def run():
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query or 'who' in query or 'what' in query or 'how' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)

            print(results)
            speak(results)

        elif 'play' in query:
            search = YoutubeSearch(f'{query} lyrical', max_results=1).videos
            yt_url = f"https://youtube.com{search[0]['url_suffix']}"
            audio_url = pytube.YouTube(yt_url).streaming_data["adaptiveFormats"][-1]["url"]
            yt_song_title = search[0]['title']
            player = vlc.MediaPlayer(audio_url)
            player.play()
            speak(f"started playing : {music.spotify_track_main_title(yt_song_title)}")
            time.sleep(2)
            while player.is_playing():
                q = takeCommand()
                if 'stop' in q:
                    player.stop()

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'open' in query:
            s = query.replace('open','')
            keyboard.press_and_release('command+space')
            keyboard.write(s)
            keyboard.press_and_release('enter')

        elif 'selfie' in query or 'pic' in query or 'photo' in query:
            speak('taking a selfie, say cheese')
            camera = cv2.VideoCapture(0)
            return_value, image = camera.read()
            time.sleep(2)
            cv2.imwrite('selfie' + '.png', image)
            del camera

        elif 'hello' in query or 'hi' in query or 'hey' in query:
            speak(random.choice(greetings))


        elif 'how are you' in query:
            speak('iam fine, hope you are also doing good')

        elif 'love' in query:
            speak('i love you too')

        elif 'quit' in query or 'exit' in query:
            break

        else:
            webbrowser.open(f'https://google.com/search?q={query}')
            speak('I could only find this about what you asked')
            run()


run()