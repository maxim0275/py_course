import os

from numpy._core.strings import upper

from src.generators import filter_by_currency, filter_by_currency_adapted, filter_by_part_description
from src.processing import filter_by_state, sort_by_date
from src.transaction_importer import reading_operations_from_csv, reading_operations_from_excel
from src.utils import get_fin_data


def main(__parameters):
    """
    отвечает за основную логику проекта и связывает функциональности между собой
    """
    text1 = """
    Программа: Привет! Добро пожаловать в программу работы
    с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""

    print(text1)
    if __parameters == "noauto":
        answer1 = input("Пользователь: ")
    else:
        answer1 = "1"

    if answer1 == "1":
        type_file = "JSON"
    elif answer1 == "2":
        type_file = "CSV"
    elif answer1 == "3":
        type_file = "XSLX"
    else:
        print("Выбран некорректный вариант")
        exit(1)

    text2 = f"Программа: Для обработки выбран {type_file}-файл."
    print(text2)

    text3 = """
    Программа: Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    answer3 = ""
    while upper(answer3) not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(text3)

        if __parameters == "noauto":
            answer3 = input("Пользователь: ")
        else:
            answer3 = "EXECUTED"

        if upper(answer3) not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Программа: Статус операции "{answer3}" недоступен.')
    print(f"Выбран фильтр по статусу {upper(answer3)}")

    text4 = "Программа: Отсортировать операции по дате? Да/Нет"
    answer4 = ""
    while answer4 not in ["Да", "Нет"]:
        print(text4)

        if __parameters == "noauto":
            answer4 = input("Пользователь: ")
        else:
            answer4 = "Да"

        if answer4 not in ["Да", "Нет"]:
            print('Ответ неверный.')

    answer5 = ""
    if answer4 == "Да":
        text5 = "Отсортировать по возрастанию или по убыванию? "
        while answer5 not in ["по возрастанию", "по убыванию"]:
            print(text5)

            if __parameters == "noauto":
                answer5 = input("Пользователь: ")
            else:
                answer5 = "по возрастанию"

            if answer5 not in ["по возрастанию", "по убыванию"]:
                print('Ответ неверный.')

    text6 = "Выводить только рублевые транзакции? Да/Нет "
    answer6 = ""
    while answer6 not in ["Да", "Нет"]:
        print(text6)

        if __parameters == "noauto":
            answer6 = input("Пользователь: ")
        else:
            answer6 = "Нет"

        if answer6 not in ["Да", "Нет"]:
            print('Ответ неверный.')

    text7 = "Отфильтровать список транзакций по определенному слову в описании? Да/Нет"
    answer7 = ""
    while answer7 not in ["Да", "Нет"]:
        print(text7)

        if __parameters == "noauto":
            answer7 = input("Пользователь: ")
        else:
            answer7 = "Нет"

        if answer7 not in ["Да", "Нет"]:
            print('Ответ неверный.')

    answer8 = ""
    if answer7 == "Да":
        while answer8 == "":
            text8 = "Введите слово для фильтра."
            print(text8)
            answer8 = input("Пользователь: ")

    dicts1 = []
    root_dir = os.path.dirname(os.path.abspath(__file__))
    if answer1 == "1":
        # читаем файл JSON
        file1_path = os.path.join(root_dir, "data", "operations.json")
        dicts1 = get_fin_data(file1_path)
    elif answer1 == "2":
        # читаем файл CSV
        file1_path = os.path.join(root_dir, "data", "transactions.csv")
        dicts1 = reading_operations_from_csv(file1_path)
    elif answer1 == "3":
        # читаем файл XLSX
        file1_path = os.path.join(root_dir, "data", "transactions_excel.xlsx")
        dicts1 = reading_operations_from_excel(file1_path)

    # данные из выбранного файла
    # print(dicts1)

    # фильтр по выбранному статусу
    dicts3 = filter_by_state(dicts1, answer3)

    # print("Отфильтрованный")
    # print(dicts3)

    if len(dicts3) == 0:
        print("Отфильрованный список пустой")
        exit(0)

    dicts5 = dicts3
    if answer4 == "Да":
        # согласились сортировать
        if answer5 == "по возрастанию":
            dicts5 = sort_by_date(dicts3, "date", False)
        else:
            dicts5 = sort_by_date(dicts3, "date", True)

    if len(dicts5) == 0:
        print("Программа: список пуст")
        exit(0)

    # print("Отфильрованный, остсортированный")
    # print(dicts5)

    dicts6 = dicts5
    if answer6 == "Да":
        # Выбрали только рублевые транзакции
        if answer1 != "1":
            dicts6 = list(filter_by_currency_adapted(dicts5, "RUB"))
        else:
            dicts6 = list(filter_by_currency(dicts5, "RUB"))

    # print("Отфильрованный, отсортированный, фильтр по валюте")
    # print(dicts6)

    if len(dicts6) == 0:
        print("Программа: список пуст")
        exit(0)

    dicts8 = dicts6
    if answer7 == "Да":
        dicts8 = filter_by_part_description(dicts6, answer8)

    if len(dicts8) > 0:
        print("Программа: Распечатываю итоговый список транзакций...")
    else:
        print("Программа: список пуст")
    print(dicts8)

    return dicts8


if __name__ == "__main__":
    main("noauto")
