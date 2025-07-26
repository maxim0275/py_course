def filter_by_currency(transactions: list, currency: str):

    """    принимает на вход список словарей
    возвращать итератор, который поочередно выдает транзакции с заданной валютой    """

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction
