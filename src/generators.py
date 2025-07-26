from typing import Iterable, Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator[str]:
    """    принимает на вход список словарей
    возвращать итератор, который поочередно выдает транзакции с заданной валютой    """

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Iterator[str]:
    """ Принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди."""
    for i in transactions:
        yield i["description"]
