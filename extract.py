import requests
import time

BASE_URL = "https://api.coinpaprika.com/v1"
COINS = [
    "btc-bitcoin",
    "eth-ethereum",
    "usdt-tether",
    "bnb-binance-coin",
    "sol-solana",
]

def extract():
    print("Starting data extraction from Coinpaprika...")
    extracted_coins = []

    for coin in COINS:
        url = f"{BASE_URL}/tickers/{coin}"
        
        try:
            print(f"Fetching: {coin}...")
            # Added a timeout so the container doesn't hang forever if the API is slow
            response = requests.get(url, timeout=10)
            
            # This forces Python to raise an error if the status code is 4xx or 5xx
            response.raise_for_status() 
            
            extracted_coins.append(response.json())
            
            # A tiny sleep interval is best practice to avoid hitting rate limits
            time.sleep(0.5)
            
        except requests.exceptions.RequestException as error:
            # If a single coin fails, we log it but don't crash the whole pipeline
            print(f"Error fetching {coin}: {error}")

    print(f"Extraction complete. Successfully pulled {len(extracted_coins)} coins.")
    return extracted_coins
