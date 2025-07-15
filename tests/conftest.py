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


@pytest.fixture
def account_1():
    return "73654108430135874305"


@pytest.fixture
def account_2():
    return "73654108430135874306"


@pytest.fixture
def account_3():
    return "7365410843013587430"


@pytest.fixture
def account_1_masked():
    return "**4305"


@pytest.fixture
def account_2_masked():
    return "**4306"

@pytest.fixture
def account_3_masked():
    return ""
