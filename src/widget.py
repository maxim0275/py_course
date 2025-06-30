from dateutil import parser
from src import masks


def mask_account_card(account_or_card: str) -> str:
    """принимает на вход номер карты или счета
    и возвращает маску
    """
    result = ""
    candidat_data = ""
    for candidat_data in account_or_card.split(" "):
        if candidat_data.isdigit():
            if len(candidat_data) == len("7000792289606361"):
                result = masks.get_mask_card_number(candidat_data)
            elif len(candidat_data) == len("73654108430135874305"):
                result = masks.get_mask_account(candidat_data)
    return account_or_card[:len(account_or_card) - len(candidat_data)] + result


def get_date(date_string: str) -> str:
    """
    принимает на вход строку и отдает корректный результат в формате
    11.07.2018
    """
    try:
        parsed_date = parser.parse(date_string)
        return parsed_date.strftime("%d.%m.%Y")
    except ValueError:
        print("Некорректный формат даты")
        return ""

    def f1():
        pass

