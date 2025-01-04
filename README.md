Iris is a Python-based voice assistant that can perform various tasks such as reading emails, playing music, fetching the weather, opening applications, and providing system information. It is designed to assist with daily activities and includes fun features like telling jokes and fun facts.

Features

Utility Functions

Read Emails: Fetch and read unread emails from your Gmail inbox.

Weather Information: Get current weather details using OpenWeather API.

System Information: Monitor CPU and RAM usage.

Set Reminders: Set reminders and get notified at a specific time.

Open Applications: Open applications like Notepad, Calculator, and more.

Entertainment

Play Music: Play music or videos on YouTube.

Tell Jokes: Lighten your mood with jokes.

Fun Facts: Hear interesting facts.

Other Features

Search Wikipedia: Get quick summaries from Wikipedia.

Open Websites: Open popular websites like YouTube and Google.

Time Query: Ask Iris for the current time.

Prerequisites

Python 3.6 or higher

Required Python Libraries:

pyttsx3

SpeechRecognition

pywhatkit

pyjokes

wikipedia

imaplib

smtplib

requests

psutil

Install the dependencies using:

pip install pyttsx3 SpeechRecognition pywhatkit pyjokes wikipedia requests psutil

Setup

Email Integration

Use your Gmail account credentials for email integration.

Enable "Less secure app access" or create an App Password in your Google account settings.

Replace the placeholders for email and password in the script:

username = "your_email@gmail.com"
password = "your_app_password"

Weather API

Sign up for a free API key at OpenWeather.

Replace the placeholder with your API key in the script:

api_key = "your_api_key"

Usage

Clone this repository:

git clone https://github.com/yourusername/iris-voice-assistant.git

Navigate to the project directory:

cd iris-voice-assistant

Run the script:

python iris.py

Interact with Iris using voice commands such as:

"Read my emails"

"What's the weather in New York?"

"Set a reminder"

"Play music"

"Tell me a joke"

Commands

Here are some sample commands you can use with Iris:

Utility

"Read my emails"

"Open YouTube"

"What's the time?"

Entertainment

"Play music"

"Tell me a fun fact"

Information

"Search Wikipedia for Python programming"

"What's the weather in London?"

Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

With Iris, simplify your daily tasks and have some fun while you're at it!
