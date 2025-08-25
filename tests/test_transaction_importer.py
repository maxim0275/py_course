import os
from unittest.mock import patch, Mock

import pytest
import pandas as pd

from src.transaction_importer import reading_operations_from_csv, reading_operations_from_excel


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


def transactions_empty() -> list:
    return [{"Nothing"}]


@patch('pandas.read_csv')
def test_reading_operations_from_csv(mock_get, transactions) -> None:
    mock_get_return_value = transactions
    mock_get.return_value = pd.DataFrame(mock_get_return_value)

    file1_path = os.path.join("data", "transactions.csv")

    assert reading_operations_from_csv(file1_path) == transactions


def test_reading_operations_from_csv_not_file():
    file1_path = os.path.join("data", "transactions1.csv")
    assert reading_operations_from_csv(file1_path) == [{"Nothing"}]


def test_reading_operations_from_csv_empty_file():
    file1_path = os.path.join("data", "transactions_1.csv")
    assert reading_operations_from_csv(file1_path) == [{"Nothing"}]


def test_reading_operations_from_csv_no_id_col():
    file1_path = os.path.join("data", "transactions.csv")
    # file1_path = os.path.join("..", "data", "transactions.csv")
    _dict = reading_operations_from_csv(file1_path)
    assert ('id' in list(_dict[2].keys())[0])


def test_reading_operations_from_csv_no_state_col():
    file1_path = os.path.join("data", "transactions.csv")
    # file1_path = os.path.join("..", "data", "transactions.csv")
    _dict = reading_operations_from_csv(file1_path)
    assert ('state' in list(_dict[2].keys())[0])


@patch('pandas.read_csv')
def test_reading_operations_from_csv_read_mock(mock_read_csv, transactions):
    mock_read_csv.return_value = pd.DataFrame(transactions)

    file1_path = os.path.join("data", "transactions.csv")
    # file1_path = os.path.join("..", "data", "transactions.csv")

    result = reading_operations_from_csv(file1_path)
    assert result == transactions


@patch('pandas.read_excel')
def test_reading_operations_from_excel(mock_get, transactions) -> None:
    mock_get_return_value = transactions
    mock_get.return_value = pd.DataFrame(mock_get_return_value)

    file2_path = os.path.join("data", "transactions_excel.xlsx")

    assert reading_operations_from_excel(file2_path) == transactions


def test_reading_operations_from_excel_not_file():
    file1_path = os.path.join("data", "transactions_excel1.xlsx")
    assert reading_operations_from_excel(file1_path) == [{"Nothing"}]


@patch('pandas.read_excel')
def test_reading_operations_from_excel_read_mock(mock_read_excel, transactions):
    mock_read_excel.return_value = pd.DataFrame(transactions)

    file1_path = os.path.join("data", "transactions_excel.xlsx")
    # file1_path = os.path.join("..", "data", "transactions_excel.xlsx")

    result = reading_operations_from_excel(file1_path)
    assert result == transactions
