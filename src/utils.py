import json

import requests


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


