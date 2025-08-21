import json
import logging

from src.external_api import get_summ_rated

utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("logs/utils.log", encoding="utf-8", mode="w")
file_handler.setFormatter(formatter)
utils_logger.addHandler(file_handler)


def get_fin_data(path_to_file):
    """
    принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях
    """
    transactions = []
    utils_logger.debug("Чтение файла с транзакциями")
    try:
        with open(path_to_file, "r", encoding="utf-8", errors="ignore") as f:
            transactions = json.load(f)
            utils_logger.debug("Файл с транзакциями прочитан")
    except Exception as e:
        print(f"Ошибка чтения файла.{e}")
        utils_logger.error("Ошибка чтения файла с транзакциями или ошибка преобразования данных")

    transactions = [transaction for transaction in transactions]

    return transactions


def get_summ_trans(transaction):
    """
    принимает на вход транзакцию и возвращает
    сумму транзакции (amount) в рублях, тип данных —float
    """
    if transaction == {}:
        utils_logger.error("Данные транзакции отсутствуют")
        return 0
    utils_logger.debug("Чтение кода валюты в транзакции")
    try:
        currency_in_transaction = transaction["operationAmount"]["currency"].get("code")
    except Exception:
        print("Некорректный словарь")
        utils_logger.error("Формат переданной транзакции некорректный. Код транзакции не прочитан")
        return -1

    amount = transaction["operationAmount"].get("amount")
    utils_logger.debug(f"Получена сумма транзакции {amount} для кода {currency_in_transaction}")
    if currency_in_transaction != "RUB":
        utils_logger.debug(f"Запрошена сконвертированная сумма для валюты {currency_in_transaction}")
        amount = get_summ_rated(currency_in_transaction, amount)
        utils_logger.debug(f"Получена сконвертированная сумма для валюты {amount} для кода валюты {currency_in_transaction}")
    return amount
