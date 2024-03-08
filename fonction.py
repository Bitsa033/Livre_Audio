import pyttsx3
from pypdf import PdfReader
from tkinter import *
from tkinter import filedialog
import random

def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))

def parler():

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[0].id) # 2 is the 3rd item index
    newVoiceRate = 145
    engine.setProperty('rate',newVoiceRate) # va lentement selon la comprhehension d'un humain
    var= " L'histoire est la connaissance du passé basé sur les écrits"
    engine.say(var) # perfect
    
    engine.runAndWait()
    
def lire_pdf(pdf):

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[0].id) # 2 is the 3rd item index
    newVoiceRate = 145
    engine.setProperty('rate',newVoiceRate) # va lentement selon la comprhehension d'un humain
    reader = PdfReader("documents/" + pdf + ".pdf")
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    var= " L'histoire est la connaissance du passé basé sur les écrits"
    engine.say(text) # perfect

    engine.runAndWait()