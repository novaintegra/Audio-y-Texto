import speech_recognition as sr
from langdetect import detect

def identificar_idioma():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo:")
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio)
        print("Transcripción:", texto)
        idioma = detect(texto)
        print("Idioma detectado:", idioma)
    except sr.UnknownValueError:
        print("No pude entender lo que dijiste")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__": 

    identificar_idioma()