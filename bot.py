from chatterbot import ChatBot
import speech_recognition as sr
import tts.sapi


voice = tts.sapi.Sapi()
chatbot = ChatBot('Boo',
    database='./db.sqlite3'
)

def speak():
    request = ""
    flag = False

    if(flag):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak:")
            audio = r.listen(source)
        try:
            request = r.recognize_google(audio)
            flag = True
        except:
            print("Could not understand audio. Try Again")
    return request

while True:
    #hange the value of wanna_speak to True if you want to talk with the bot instead of chatting
    wanna_speak= False
    if(wanna_speak):
        request = speak()
    else:
        request = input("You: ")

    response = chatbot.get_response(request)
    print("Boo: ",response)
    if(wanna_speak):
        voice.say(response)

