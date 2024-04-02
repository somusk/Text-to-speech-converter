from gtts import gTTS 
from playsound import playsound 

fileName = "sample.mp3"
textInput = input("Enter any text: ")
language = input("Enter language type: ")

convertingAudio = gTTS(text=textInput, lang=language, slow=True)
convertingAudio.save(fileName)
playsound(fileName)


