from datetime import datetime
from functools import wraps


def log(filename=None):
    def decorator(func):
        """
        логируется начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
        принимаются необязательный аргумент filename
        , который определяет, куда будут записываться логи (в файл или в консоль)
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                time_1 = datetime.now().time()
                time_2 = "None"
                result = func(*args, **kwargs)
                time_2 = datetime.now().time()
                name_func = func.__name__
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"Начало: {time_1}" + "\n")
                        file.write(f"Функция {name_func} ок. Результат: {result}" + "\n")
                        file.write(f"Конец: {time_2}" + "\n")
                        file.write("\n")
                else:
                    print(f"Начало: {time_1}")
                    print(f"Функция {name_func} ок. Результат: {result}" + "\n")
                    print(f"Конец: {time_2}")
            except ZeroDivisionError:
                result = "faulty_function error: division by zero"
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"Начало: {time_1}")
                        file.write(f"{func.__name__} error: ZeroDivisionError. Inputs: {args}, {kwargs}")
                        file.write(f"Конец: {time_2}")
                else:
                    print(f"Начало: {time_1}")
                    print(f"{func.__name__} error: ZeroDivisionError. Inputs: {args}, {kwargs}")
                    print(f"Конец: {time_2}")
            except Exception as e:
                result = None
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"Начало: {time_1}")
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                        file.write(f"Конец: {time_2}")
                else:
                    print(f"Начало: {time_1}")
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                    print(f"Конец: {time_2}")
            return result

        return wrapper

    return decorator
