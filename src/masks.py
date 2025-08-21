import logging

masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("logs/masks.log", encoding="utf-8", mode="w")
file_handler.setFormatter(formatter)
masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу
    # XXXX XX** **** XXXX
    """
    card_number_masked = ""
    masks_logger.debug("Проверка длины номера карты")
    if len(card_number) == len("7000792289606361"):
        card_number_masked = (
            card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[len(card_number) - 4:]
        )
        masks_logger.debug("Длина номера карты корректная")
    else:
        masks_logger.error("Длина номера карты некорректная")
    return card_number_masked


def get_mask_account(account: str) -> str:
    """принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    # **XXXX
    """
    account_masked = ""
    masks_logger.debug("Проверка длины номера счета")
    if len(account) == len("73654108430135874305"):
        masks_logger.debug("Длина номера счета корректная")
        account_masked = "**" + account[len(account) - 4:]
    else:
        masks_logger.error("Длина номера счета некорректная")
    return account_masked
