import os

import requests
from dotenv import load_dotenv


def get_exchange_rate(currency, amount):
    to = "RUB"
    _from = currency
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={_from}&amount={amount}"
    payload = {}

    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    headers = {
        "apikey": API_KEY
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text

    if response.status_code != 200:
        return False, {}
    return 0
