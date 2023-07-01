import speech_recognition as sr
import winsound
import pyttsx3
import wikipedia

voice = pyttsx3.init()

your_voice = sr.Recognizer()  # Create object that record voice

with sr.Microphone() as source:  # Using Microphone to put the voice input

    winsound.Beep(1500, 500)  # Start record voice
    audio = your_voice.listen(source)  # Get the voice
    winsound.Beep(1500, 500)  # End record voice

try:
    In = your_voice.recognize_google(audio, language='en')
    print(In)
    result = wikipedia.summary(In, sentences=3)
    print(result)
    voice.say(result)
    voice.runAndWait()
except Exception as err:
    print(err)
