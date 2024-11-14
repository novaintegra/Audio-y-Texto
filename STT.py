#pip install pydub SpeechRecognition
#pip install PyAudio;

import speech_recognition as sr
from pydub import AudioSegment

# Inicializar el reconocedor de voz
r = sr.Recognizer()

# Función para convertir un archivo de audio a formato compatible con SpeechRecognition
def convert_audio(audio_file):
    sound = AudioSegment.from_mp3(audio_file)
    sound.export("temp.wav", format="wav")
    return "temp.wav"

# Especificar el archivo de audio
audio_file = "Grabacion.wav"  # Reemplaza con la ruta de tu archivo

# Convertir el audio a formato WAV
wav_file = convert_audio(audio_file)

# Utilizar el reconocedor para transcribir el audio
with sr.AudioFile(wav_file) as source:
    audio_data = r.record(source)
    try:
        text = r.recognize_google(audio_data, language="es-ES")  # Cambia "es-ES" por el idioma deseado
        print(text)
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print("Error del servicio de reconocimiento de voz; {0}".format(e))