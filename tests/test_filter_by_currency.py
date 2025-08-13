import pytest

from src.generators import filter_by_currency


@pytest.mark.parametrize(
    "transactions, currency_code, expected",
    [
        (
            [
                {"id": 1, "operationAmount": {"amount": "90.00", "currency": {"code": "USD"}}},
                {"id": 2, "operationAmount": {"amount": "20.00", "currency": {"code": "EUR"}}},
                {"id": 3, "operationAmount": {"amount": "96.00", "currency": {"code": "USD"}}},
            ],
            "USD",
            [
                {"id": 1, "operationAmount": {"amount": "90.00", "currency": {"code": "USD"}}},
                {"id": 3, "operationAmount": {"amount": "96.00", "currency": {"code": "USD"}}},
            ],
        ),
        (
            [
                {"id": 1, "operationAmount": {"amount": "90.00", "currency": {"code": "EUR"}}},
                {"id": 2, "operationAmount": {"amount": "20.00", "currency": {"code": "EUR"}}},
                {"id": 3, "operationAmount": {"amount": "96.00", "currency": {"code": "EUR"}}},
            ],
            "USD",
            [],
        ),
        (
            [
                {"id": 1, "operationAmount": {"amount": "80.00", "currency": {"code": "USD"}}},
                {"id": 2, "operationAmount": {"amount": "20.00", "currency": {"code": "EUR"}}},
                {"id": 3, "operationAmount": {"amount": "50.00", "currency": {"code": "USD"}}},
            ],
            "",
            [],
        ),
        ([], "USD", []),
        ("", "USD", ["Список не найден"]),
    ],
)
def test_filter_by_currency(transactions, currency_code, expected):
    result = list(filter_by_currency(transactions, currency_code))
    assert result == expected
