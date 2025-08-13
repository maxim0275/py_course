from functools import wraps


def log(filename=None):
    def decorator(func):
        """
        логируется начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
        принимаются необязательный аргумент filename
        , который определяет, куда будут записываться логи (в файл или в консоль)
        """

        @wraps(func)
        def wrapper(*args: str, **kwargs: str):
            try:
                result = func(*args, **kwargs)
                name_func = func.__name__
                if filename:
                    file = open(filename, "a", encoding="utf-8")
                    file.write(f"Функция {name_func} ок. Результат: {result}" + "\n")
                    file.close()
                else:
                    print(f"{name_func} ок. Результат: {func(*args, **kwargs)}")
            except Exception as e:
                result = None
                print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
            except ZeroDivisionError:
                result = None
                print(f"{func.__name__} error: ZeroDivisionError. Inputs: {args}, {kwargs}")
            except KeyError:
                result = None
                print(f"{func.__name__} error: KeyError. Inputs: {args}, {kwargs}")
            return result

        return wrapper

    return decorator
