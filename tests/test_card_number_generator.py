import pytest

from src.generators import card_number_generator


@pytest.mark.parametrize("start, stop, expected", [
    (1, 5, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004"
    ]),
    (pytest.param(9999999999999995, 10000000000000000, [
        "9999 9999 9999 9995",
        "9999 9999 9999 9996",
        "9999 9999 9999 9997",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999"
    ], marks=pytest.mark.xfail))
])
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected
