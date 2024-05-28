import pyttsx3
speech=pyttsx3.init()
text=input("Enter the text to convert to speech")
speech.say(text)
speech.runAndWait()
#pip install pyttsx3