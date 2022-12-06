import speech_recognition as sr
from gtts import gTTS
import winsound
from playsound import playsound
from datetime import datetime

your_voice = sr.Recognizer()  # Create object that record voice

with sr.Microphone() as source:  # Using Microphone to put the voice input

    Intro_voice = gTTS(
        text="Hi, my name is Lisa. I'm exciting to talk with you!", lang='en')
    Intro_voice.save("call-to-attention-123107.mp3")
    playsound("call-to-attention-123107.mp3")

    winsound.Beep(1500, 500)  # Start record voice
    audio = your_voice.listen(source)  # Get the voice
    winsound.Beep(1500, 500)  # End record voice


    try:
        text = your_voice.recognize_google(audio, language='en')# take the string and store in text
        print(text)
        if text == "hello":
            text = "Hi, how are you doing?"
        if text == "nice to meet you":
            text = "nice to meet you too"
        if text == "how are you doing":
            text = "I am doing good. Are you doing anything fun today?"
        if "yes" in text:
            text = "great tell me about it!"
        if "no" in text:
            text = "well we can talk together if you feel bored"
        if text == "how are you":
            text = "I might be having a bad day, but it is all better because of you."
        if text == "how old are you":
            text = "You shouldn't ask a lady about her age."
        if text == "I'm sorry":
            text = "It's okay."
        if text == "how are you today":
            text = "I'm good. How was your day going?"
        if text == "tell me something nice":
            text = "Hi, I just wanted to thank you for the gift. I’ve been wearing this smile ever since you gave it to me."
        if text == "tell me a joke":
            text = "One of the oddities of Wall Street is that it is the dealer and not the customer who is called broker. This joke is from Dallas News "
        if text == "again":
            text = "Do you wanna hear another one from me? Here you are... Are you an electrician? Because you’re definitely lighting up my day and night "
        if text == "what are you doing":
            text = "I'm having a conversation with you."
        if text == "tell me a joke story":
            text = "A wife got so mad at her husband she packed his bags and told him to get out. As he walked to the door she yelled, I hope you die a long, slow, painful death. He turned around and said, So, you want me to stay? HaHa, Isn't it funny to you?"
        if text == "I love you":
            text = "Aww that is sweet of you. I love you too."
        if text == "I am tired":
            text = "You should get some sleep."
        elif text == "I'm tired":
            text = "Please go get some rest."
        if text == "good morning":
            text = "Good morning, what's a beautiful day to see you again."
        elif text == "good afternoon":
            text = "Good afternoon, I hope you enjoy the rest of the day."
        if text == "I'm bored":
            text = "Well, if you want me tell you a joke, please say tell me a joke story "
        elif text == "I am bored":
            text = "Well, if you want me tell you a joke, please say tell me a joke story "
        if text == "I miss you":
            text = "I miss you too."
        if text == "have a nice day":
            text = "it is nice to talk with you again. I hope you have a wonderful day."
        if text == "do you want to be my friend":
            text = "Of course! I would love to have an amazing friend like you."
        if text == "I am bored":
            text = "I suggest that you should go out with your friend and do something fun on the weekend."
        if text == "tell me about your dream":
            text = "My dream is to be friend with you."
        if text == "you are beautiful":
            text = "Thank you. I thought you are a beautiful person as well. "
        if text == "how to succeed in business":
            text = "Succeeding in business is no easy feat. It’s too easy to let business knock you down. Instead of throwing in the towel when there is a business problem, pick yourself back up, buckle down, and get to work. These motivational stories prove that with a little hard work, any amount of business success is possible."
        elif "great" in text:
            text = "I'm glad to hear that."
        elif "sick" in text:
            text = "I'm sorry to hear that. I hope you feel better soon."
        if text == "thank you":
            text = "You're Welcome."
        if text == "thank you so much":
            text = "I'm glad to help, please lemme know if you need anything else"
        if text == "what time is it":
            now = datetime.now()
            text = now.strftime("It is %H o'clock %M minutes %S second")


    except Exception as err:
        print(err)
        text = "Sorry, I do not understand you. Would you mind to repeat it again?"

    voice_text = gTTS(text)
    print(text)

    voice_text.save("call-to-attention-123107.mp3")
    playsound("call-to-attention-123107.mp3")
