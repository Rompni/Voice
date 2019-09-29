from gtts import gTTS
from playsound import playsound


def tts(text_file, lang, name_file):
    with open(text_file, "r") as file:
        text = file.read()
    file = gTTS(text=text, lang=lang)
    filename = name_file
    file.save(filename)


def media(file):
    playsound(file)