def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу
    # XXXX XX** **** XXXX
    """
    card_number_masked = ""
    if len(card_number) == len("7000792289606361"):
        card_number_masked = (
                card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[len(card_number) - 4:]
        )
    return card_number_masked


def get_mask_account(account: str) -> str:
    """принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    # **XXXX
    """
    account_masked = ""
    if len(account) == len("73654108430135874305"):
        account_masked = "**" + account[len(account) - 4:]
    return account_masked
