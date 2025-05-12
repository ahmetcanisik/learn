import cowsay
import pyttsx3

engine = pyttsx3.init()

engine.setProperty('voices', "com.apple.voice.compact.tr-TR.Yelda")

this = input("What's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()