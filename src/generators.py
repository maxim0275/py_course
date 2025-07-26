from typing import Any, Generator


def filter_by_currency(transactions: list, currency_code: str) -> Generator[Any, None, None | list[Any] | str]:
    """    принимает на вход список словарей
    возвращать итератор, который поочередно выдает транзакции с заданной валютой    """

    if not isinstance(transactions, list):
        yield "Список не найден"
    elif not currency_code or transactions == []:
        return ""

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction
    return None


def transaction_descriptions(transactions: list) -> Generator[str | Any, None, str | None]:
    """ Принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди."""

    if not isinstance(transactions, list):
        yield "Список не найден"
    elif len(transactions) == 0:
        yield "Пустой список"

    for i in transactions:
        yield i["description"]
    return None


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """ Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X  — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров."""
    if bool(isinstance(start, int)) and bool(
            isinstance(stop, int)) and start <= stop and start >= 1 and stop <= 9999999999999999:
        for i in range(start, stop):
            card_number = str(i).zfill(16)
            yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
    else:
        yield 'Неверно заданы параметры для номер карты'
