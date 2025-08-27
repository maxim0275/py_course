from collections import Counter

import pytest

from src.process_bank import process_bank_search, process_bank_operations


@pytest.fixture
def transactions() -> list:
    return [
        {
            'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0,
            'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'
        },
        {
            'id': 3598919.0, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740.0,
            'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
            'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'
        }
    ]


@pytest.fixture
def categories() -> list:
    return ["Перевод организации", "Перевод с карты на карту"]


def test_process_bank_search_empty_src():
    result = process_bank_search([], "str")
    assert result == []


def test_process_bank_search_not_empty_src(transactions):
    result = process_bank_search(transactions, "организации")
    assert result == [
        {
            'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0,
            'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'
        }]


def test_process_bank_operations_success(transactions, categories):
    result = process_bank_operations(transactions, categories)
    assert result == Counter({'Перевод организации': 1, 'Перевод с карты на карту': 1})


def test_process_bank_operations_fail1(transactions, categories):
    with pytest.raises(ValueError) as excinfo:
        process_bank_operations([], categories)
    assert "Список словарей пуст" in str(excinfo.value)


def test_process_bank_operations_fail2(transactions, categories):
    with pytest.raises(ValueError) as excinfo:
        process_bank_operations(transactions, [])
    assert "Список категорий пуст" in str(excinfo.value)
