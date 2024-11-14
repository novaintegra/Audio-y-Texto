#pip install pyttsx3
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice and rate (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change the index to select a different voice   

engine.setProperty('rate', 150)  # Adjust the speaking rate

# Text to be spoken
text = "Este es una prueba de como se convierte texto en voz."

# Speak the text
engine.say(text)
engine.runAndWait()