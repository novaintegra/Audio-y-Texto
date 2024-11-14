import requests
from bs4 import BeautifulSoup

url = "https://eltiempo.com"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar todos os elementos que contêm o nome
titulares = soup.find_all('h3', {'class': 'c-article__title'})



# Imprimir os nomes
for titular in titulares:
    print(titular.text.strip())