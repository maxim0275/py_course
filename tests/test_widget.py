import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("src_date, dst_date", [("src_date_1", "dst_date_1"), ("src_date_2", "dst_date_2")])
def test_get_date(src_date: str, dst_date: str, request: pytest.FixtureRequest) -> None :
    src_date_requested = request.getfixturevalue(src_date)
    dst_date_requested = request.getfixturevalue(dst_date)
    assert get_date(src_date_requested) == dst_date_requested


@pytest.mark.parametrize(
    "param, result", [("7000792289606361", "7000 79** **** 6361"), ("73654108430135874305", "**4305")]
)
def test_mask_account_card(param: str, result: str) -> None :
    assert mask_account_card(param) == result
