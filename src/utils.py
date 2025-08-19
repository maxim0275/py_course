import json

import requests

from src.external_api import get_summ_rated


def get_github_users(users):
    results = []
    for user in users:
        status, user_data = get_user_info(user)

    return 1


def get_user_info(user):
    result = requests.get(f"https://api.github.com/users/{user}")
    if result.status_code != 200:
        status = False
    else:
        status = True

    return "1", "1"


def get_fin_data(path_to_file):
    """
    принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях
    """
    transactions = []
    try:
        with open(path_to_file, 'r', encoding='utf-8', errors='ignore') as f:
            transactions = json.load(f)
    except Exception as e:
        print(f"Ошибка чтения файла.{e}")

    transactions = [transaction for transaction in transactions]

    return transactions

def get_summ_trans(transaction):
    """
    принимает на вход транзакцию и возвращает
    сумму транзакции (amount) в рублях, тип данных —float
    """
    if transaction == {}:
        return 0
    currency_in_transaction = transaction["operationAmount"]['currency'].get('code')
    amount = transaction["operationAmount"].get('amount')
    if currency_in_transaction != 'RUB':
        amount2 = get_summ_rated(currency_in_transaction, amount)

    return amount
