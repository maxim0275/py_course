import pytest

from src.masks import get_mask_account


@pytest.mark.parametrize(
    "account, account_masked",
    [("account_1", "account_1_masked"), ("account_2", "account_2_masked"), ("account_3", "account_3_masked")],
)
def test_account(account: str, account_masked: str, request: pytest.FixtureRequest) -> None:
    account_requested = request.getfixturevalue(account)
    account_masked_requested = request.getfixturevalue(account_masked)
    assert get_mask_account(account_requested) == account_masked_requested
