import os

from dotenv import load_dotenv
from requests import request


def get_summ_rated(currency, amount):
    to = "RUB"
    _from = currency
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={_from}&amount={amount}"
    payload = {}
    load_dotenv()
    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}
    response = request("GET", url, headers=headers, data=payload)
    result = 0
    if response.status_code == 200:
        result_json = response.json()
        result = result_json["result"]
    return result
