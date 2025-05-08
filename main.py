import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.coingecko.com/api/v3"

header = {
    "accept": "application/json"
}
user_coin = input("Welcome to the Crypto Price Tracker, Enter the coin symbol(e.g, bitcoin, ethereum): ").lower()


parameter = {
    "vs_currencies": "usd",
    "ids": user_coin,
    "include_market_cap": "true",
    "include_24hr_vol": "true",
    "include_24hr_change": "true"
}

try:
    response = requests.get(url="https://api.coingecko.com/api/v3/simple/price", headers=header, params=parameter)
    response.raise_for_status()
    data = response.json()

    if user_coin in data:
        print(f"UserCoin: {user_coin}\nPrice: {data[user_coin]["usd"]}\nMarketCap: {data[user_coin]["usd_market_cap"]}\n24 Volume Change: {data[user_coin]["usd_24h_change"]} ")

except KeyError:
    print("You Check the name of the Coin you wrote it's Incorrect. Thank you")
except requests.RequestException as e:
    print(f"network error: {e}")

