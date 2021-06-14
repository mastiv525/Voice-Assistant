import pyttsx3
import datetime
from datetime import date
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import urllib.request
import re
import smtplib
from googlesearch import search


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def search_wikipedia(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=3)
    speak("according to Wikipedia")
    print(results)
    speak(results)


# def search_on_google():
#     speak("What are you looking for")
#     query = input("What are you looking for: ")
#
#     for i in search(query, ld='co.in', lang='en', num=10, start=0, stop=None, pause=2):
#         print(i)


def google_chrome():
    speak("I'm opening Chrome")
    os.startfile(chromePath)


def youtube():
    speak("I'm opening You Tube")
    os.startfile(chromePath)
    webbrowser.open(yt)


def music():
    speak("I'm playing the music")
    songs = os.listdir(music_dir)
    print(songs)
    os.startfile(os.path.join(music_dir, songs[0]))


def time():
    str_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {str_time}")
    print(str_time)


def current_date():
    str_date = date.today()
    speak(f"Sir, the date today is {str_date}")
    print(f"{str_date}")


def today():
    time()
    current_date()


def email():
    gmail_user = input("Wprowadź swój email: ")
    gmail_password = input("Wprowadź hasło: ")
    recipient = input("Wprowadź adres email odbiorcy: ")
    subject = input("Wprowadź tytuł: ")
    body = input("Wprowadź treść maila: ")

    sent_from = gmail_user
    to = recipient

    email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, to, subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email sent!')
    except:
        print('Something went wrong...')


def yt_search():
    speak("What video you looking for")
    search_keyword = input("Podaj nazwę wideo: ")
    search_nospaces = search_keyword.replace(" ", "+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_nospaces)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    os.startfile(chromePath)
    webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[0])
    speak("Here we go")


def shutdown():
    speak("Shutdown will take place in a minute")
    print("Shutdown will take place in a minute")
    os.system('cmd /k "shutdown /s"')


def reboot():
    speak("Reboot will take place in a minute")
    print("Reboot will take place in a minute")
    os.system('cmd /k "shutdown /r"')


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour < 12:
        speak("Good morning")
    elif 12 <= hour < 18:
        speak("Hello")
    elif 18 <= hour < 24:
        speak("Good afternoon")
    else:
        speak("Go to sleep")

    speak("Hi I am Friday Sir. Please tell me how can I help you")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


if __name__ == '__main__':
    chromePath = input("Wprowadź ścieżkę do Chrome: ") or "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    music_dir = input("Wprowadź ścieżkę do muzyki: ") or "D:\\muzyka"
    yt = 'https://www.youtube.com/'
    chrome_alias = ['open chrome', 'chrome', 'open google', 'google']
    youtube_alias = ['open youtube', 'youtube', 'yt']
    music_alias = ['play music', 'music', 'songs', 'play song', 'play songs']
    time_alias = ['the time', 'time', 'hour', 'clock']
    date_alias = ['date', 'the date', 'calendar']
    email_alias = ['email', 'mail', 'send mail', 'send message', 'gmail']
    today_alias = ['today', 'current day']
    shutdown_alias = ['shutdown', 'turn off', 'close']
    reboot_alias = ['restart', 'reboot']
    wish_me()
    while True:
        command = input("")
#       command = take_command().lower()
        if 'wikipedia' in command:
            search_wikipedia(command)

        elif any(alias in command for alias in chrome_alias):
            google_chrome()

        elif any(alias in command for alias in youtube_alias):
            youtube()

        elif any(alias in command for alias in music_alias):
            music()

        elif any(alias in command for alias in time_alias):
            time()

        elif any(alias in command for alias in date_alias):
            current_date()

        elif any(alias in command for alias in email_alias):
            email()

        elif any(alias in command for alias in today_alias):
            today()

        # elif 'phrase':
        #     search_on_google()

        elif 'search video':
            yt_search()

        elif any(alias in command for alias in shutdown_alias):
            shutdown()

        elif any(alias in command for alias in reboot_alias):
            reboot()


