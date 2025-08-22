from datetime import datetime


def filter_by_state(list_of_dict: list, state: str = "EXECUTED") -> list:
    """
    принимает список словарей и значение для ключа state,
    возвращает новый список словарей, отфильтрованный по state
    """
    filtered_list = []
    for dict_item in list_of_dict:
        if dict_item.get("state") == state:
            filtered_list.append(dict_item)
        else:
            continue
    return filtered_list


def sort_by_date(data_list: list, data_key: str = "date", descending: bool = True) -> list:
    """
    принимает список словарей и параметр сортировки,
    возвращает новый список, отсортированный по дате (date)
    """
    return sorted(data_list, key=lambda x: datetime.strptime(x[data_key], "%Y-%m-%dT%H:%M:%S.%f"), reverse=descending)
