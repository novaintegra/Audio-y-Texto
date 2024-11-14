##pip install pydub SpeechRecognition
import speech_recognition as sr

# Inicializar el reconocedor
r = sr.Recognizer()

# Función para escuchar el audio
def escuchar():
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)

        try:
            texto = r.recognize_google(audio)
            print("Dijiste: " + texto)

            # Aquí agregaríamos la lógica para identificar al speaker
            # Por ejemplo, comparar el texto con una base de datos de frases típicas
            # o analizar las características acústicas del audio

        except sr.UnknownValueError:
            print("No entendí")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Llamar a la función para escuchar
escuchar()