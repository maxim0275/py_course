import os
import pandas as pd


def reading_operations_from_csv(file_path: str, encoding: str = "utf-8") -> list[set[str]] | list[dict]:
    """Преобразование файла из CSV в словарь"""
    if not os.path.isfile(file_path):
        print("Файл не существует")
        return [{"Nothing"}]
    try:
        dataframe = pd.read_csv(file_path, encoding=encoding, sep=";")
        _dict = dataframe.to_dict("records")
    except Exception:
        print("Ошибка чтения файла")
        return [{"Nothing"}]

    return _dict


def reading_operations_from_excel(file_path: str) -> list[set[str]] | list[dict]:
    """Преобразование файла из EXCEL в словарь"""
    if not os.path.isfile(file_path):
        print("Файл не существует")
        return [{"Nothing"}]
    try:
        dataframe = pd.read_excel(file_path, engine="openpyxl")
    except Exception:
        print("Ошибка чтения файла")
        return [{"Nothing"}]

    return dataframe.to_dict("records")
