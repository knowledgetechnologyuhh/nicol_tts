import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)   
engine.say("Simple is better than complex. Complex is better than complicated.")

engine.runAndWait()