import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "card_number, card_number_masked",
    [("card_number_1", "card_number_1_masked"), ("card_number_2", "card_number_2_masked")],
)
def test_card_number(card_number: str, card_number_masked: str, request: pytest.FixtureRequest) -> None :
    card_number_requested = request.getfixturevalue(card_number)
    card_number_masked_requested = request.getfixturevalue(card_number_masked)
    assert get_mask_card_number(card_number_requested) == card_number_masked_requested
