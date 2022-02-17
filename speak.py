import pyttsx3
# text to speech
def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    print(voices[1].id)
    engine.setProperty('voice', voices[1].id)
    # engine.setProperty('rate', 120)
    engine.say(audio)
    print(audio)
    engine.runAndWait()