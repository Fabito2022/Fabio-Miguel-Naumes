import streamlit as st
import requests 

# Configurações da API

API_KEY = 'I4Q8KQCH25KWOAK5'
BASE_URL = 'https://www.alphavantage.co/query'

# Função para buscar dados em tempo real
def get_crypto_price(symbol):
    params = {
        'function': 'CURRENCY_EXCHANGE_RATE',
        'from_currency': symbol,
        'to_currency': 'USD',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    return float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

# Configurar o dashboard
st.title('Dashboard de Criptomoedas')

# Criptomoedas
cryptos = ['BTC', 'ETH', 'LTC']
prices = {crypto: get_crypto_price(crypto) for crypto in cryptos}

# Exibir preços
for crypto, price in prices.items():
    st.metric(label=f'{crypto}/USD', value=f'${price:.2f}')