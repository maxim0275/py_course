from typing import Iterable, Iterator, Generator


def filter_by_currency(transactions: list, currency: str) -> Generator[str, None, None]:
    """    принимает на вход список словарей
    возвращать итератор, который поочередно выдает транзакции с заданной валютой    """

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Generator[str, None, None]:
    """ Принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди."""
    for i in transactions:
        yield i["description"]

def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """ Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X  — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров."""
    for i in range(start, stop):
        card_number = str(i).zfill(16)
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"