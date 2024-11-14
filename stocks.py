#pip install yfinance

import yfinance as yf

STK = input("Escriba la acción: ")  #AAPL nvda

data = yf.Ticker(STK).history(period = "1d")


ultimo_precio_mercado = data["Close"].iloc[-1]

print("último precio mercado:",ultimo_precio_mercado)