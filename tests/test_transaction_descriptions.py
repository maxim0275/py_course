import pytest

from src.generators import transaction_descriptions


@pytest.mark.parametrize(
    "expected",
    [
        [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        ]
    ],
)
def test_transaction_descriptions(transactions, expected):
    result = list(transaction_descriptions(transactions))
    assert result == expected


@pytest.mark.parametrize("expected", [["Пустой список"]])
def test_transaction_descriptions_empty(transactions_empty, expected):
    result = list(transaction_descriptions(transactions_empty))
    assert result == expected
