import pytest


@pytest.fixture
def card_number_1() -> str:
    return "7000792289606361"


@pytest.fixture
def card_number_2() -> str:
    return "7000792289606362"


@pytest.fixture
def card_number_1_masked() -> str:
    return "7000 79** **** 6361"


@pytest.fixture
def card_number_2_masked() -> str:
    return "7000 79** **** 6362"


@pytest.fixture
def account_1() -> str:
    return "73654108430135874305"


@pytest.fixture
def account_2() -> str:
    return "73654108430135874306"


@pytest.fixture
def account_3() -> str:
    return "7365410843013587430"


@pytest.fixture
def account_1_masked() -> str:
    return "**4305"


@pytest.fixture
def account_2_masked() -> str:
    return "**4306"


@pytest.fixture
def account_3_masked() -> str:
    return ""


@pytest.fixture
def src_date_1() -> str:
    return "2018-07-11T02:26:18.671407"


@pytest.fixture
def dst_date_1() -> str:
    return "11.07.2018"


@pytest.fixture
def src_date_2() -> str:
    return "2018-07-12T02:26:18.671407"


@pytest.fixture
def dst_date_2() -> str:
    return "12.07.2018"


@pytest.fixture
def filter_state_src_list() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def filter_state_param_filter() -> str:
    return "EXECUTED"


@pytest.fixture
def filter_state_dst_list() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort_by_date_src_list() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sort_by_date_dst_list() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
