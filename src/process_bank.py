import os
import re
from collections import Counter
from typing import List, Any

from src.transaction_importer import reading_operations_from_excel


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    result = []
    result = list(filter(lambda x: re.search(search, x["Описание"]), data))
    return result


root_dir = os.path.dirname(os.path.abspath(__file__))
file2_path = os.path.join("..", "data", "operations.xlsx")
dicts = reading_operations_from_excel(file2_path)
# print(process_bank_search(dicts, "Колхоз"))


def process_bank_operations(data: list[dict], categories: list) -> list[Any]:
    result = []

    """Возвращает словарь с количеством операций в каждой категории"""
    if not data:
        raise ValueError("Список словарей пуст")
    elif not categories:
        raise ValueError("Список категорий пуст")
    else:
        result = []

        for dict_ in data:
            description = dict_.get("Категория", "")
            if description in categories:
                result.append(description)

    counted = Counter(result)

    return result


categories = []
for _dict in dicts:
    if _dict["Категория"] not in categories:
        categories.append(_dict["Категория"])

# print(categories)

print(process_bank_operations(dicts, categories))