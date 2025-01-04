import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
import pyjokes
import wikipedia
import datetime
import webbrowser
import smtplib
import imaplib
import email
import requests
import psutil
import os
import time
from email.header import decode_header
from datetime import timedelta

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    """Function to greet the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Iris, your personal assistant. How can I help you today?")

def take_command():
    """Function to listen to the user's voice and convert it into text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="en-in")
        print(f"Command: {command}\n")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that. Can you repeat?")
        return ""
    except sr.RequestError:
        print("Sorry, I'm having trouble connecting to the service. Try again later.")
        return ""

def take_action(command):
    """Function to perform actions based on the user's command."""
    if 'play music' in command:
        speak("Sure! Playing music for you.")
        kit.playonyt('music')  # This plays the first video result for 'music' on YouTube.
    
    elif 'open youtube' in command:
        speak("Opening YouTube for you.")
        webbrowser.open("https://www.youtube.com")
    
    elif 'open google' in command:
        speak("Opening Google.")
        webbrowser.open("https://www.google.com")
    
    elif 'search wikipedia' in command:
        speak("Searching Wikipedia.")
        command = command.replace('search wikipedia', '')
        result = wikipedia.summary(command, sentences=2)
        speak("According to Wikipedia, " + result)
    
    elif 'tell a joke' in command:
        speak(pyjokes.get_joke())
    
    elif 'tell a fun fact' in command:
        speak("Here's a fun fact: A shrimp's heart is in its head!")
    
    elif 'what is the time' in command:
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {str_time}")
    
    elif 'exit' in command or 'quit' in command:
        speak("Goodbye! Have a great day!")
        exit()

    elif 'read my emails' in command:
        speak("Fetching your unread emails...")
        read_emails()

    elif 'weather' in command:
        speak("Fetching the weather report...")
        get_weather()

    elif 'system info' in command:
        speak("Here is your system information...")
        get_system_info()

    elif 'set reminder' in command:
        speak("What is the reminder?")
        reminder = take_command()
        speak("When should I remind you? Please say the time in hours and minutes.")
        reminder_time = take_command()
        set_reminder(reminder, reminder_time)

    elif 'open notepad' in command:
        os.system("notepad.exe")

    elif 'open calculator' in command:
        os.system("calc.exe")

def read_emails():
    """Fetch and read unread emails from Gmail."""
    try:
        # Your Gmail credentials
        username = "your_email@gmail.com"
        password = "your_app_password"  # Use an app password for Gmail
        # Connect to the Gmail IMAP server
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(username, password)
        mail.select("inbox")
        
        # Search for unread emails
        status, messages = mail.search(None, 'UNSEEN')
        
        if status == "OK":
            email_ids = messages[0].split()
            if email_ids:
                latest_email_id = email_ids[-1]
                _, msg_data = mail.fetch(latest_email_id, "(RFC822)")
                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        subject, encoding = decode_header(msg["Subject"])[0]
                        if isinstance(subject, bytes):
                            subject = subject.decode(encoding or "utf-8")
                        speak(f"You have a new email with the subject: {subject}")
            else:
                speak("No new unread emails.")
        mail.logout()
    except Exception as e:
        speak("There was an error accessing your emails.")
        print(str(e))

def get_weather():
    """Fetch weather information using OpenWeather API."""
    api_key = "your_api_key"  # Replace with your OpenWeather API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("What's the city name?")
    city = take_command().lower()
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    
    try:
        response = requests.get(complete_url)
        data = response.json()
        if data["cod"] == "404":
            speak("City not found.")
        else:
            main = data["main"]
            weather_desc = data["weather"][0]["description"]
            temp = main["temp"]
            speak(f"The temperature in {city} is {temp} degrees Celsius with {weather_desc}.")
    except Exception as e:
        speak("Sorry, I couldn't fetch the weather right now.")
        print(str(e))

def get_system_info():
    """Fetch system information like CPU and RAM usage."""
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    speak(f"Your system is using {cpu}% of the CPU and {ram}% of the RAM.")

def set_reminder(reminder, reminder_time):
    """Set a reminder and notify the user at the given time."""
    try:
        time_parts = reminder_time.split()
        hours = int(time_parts[0])
        minutes = int(time_parts[1])
        current_time = datetime.datetime.now()
        reminder_time = current_time + timedelta(hours=hours, minutes=minutes)
        speak(f"Setting a reminder for {reminder} at {reminder_time.strftime('%H:%M:%S')}.")
        
        time.sleep((reminder_time - current_time).total_seconds())
        speak(f"Reminder: {reminder}")
    except Exception as e:
        speak("There was an error setting the reminder.")
        print(str(e))

def main():
    wish_me()
    
    while True:
        command = take_command()
        
        if command:
            take_action(command)

if __name__ == "__main__":
    main()
