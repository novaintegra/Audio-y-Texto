#pip install textblob

from textblob import TextBlob

text = input('Escriba una frase:')

blob = TextBlob(text)

print(f"Texto: {text}")

polaridad, subjetividad = blob.polarity, blob.subjectivity

print(f'Polaridad: {polaridad} Subjetividad:{subjetividad}')