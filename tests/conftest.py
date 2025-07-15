import pytest


@pytest.fixture
def card_number_1():
    return "7000792289606361"


@pytest.fixture
def card_number_2():
    return "7000792289606362"


@pytest.fixture
def card_number_1_masked():
    return "7000 79** **** 6361"


@pytest.fixture
def card_number_2_masked():
    return "7000 79** **** 6362"
