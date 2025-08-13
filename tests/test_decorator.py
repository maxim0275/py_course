import os
#import pytest
from src.decorators import log


@log()
def my_function(x, y):
    return x / y


def test_my_function_success(capsys) -> None:
    """
    Проверка успешного выполнения функции
    """
    result = my_function(4, 2)
    assert result == 2
    captured = capsys.readouterr()
    assert "my_function ок. Результат: 2" in captured.out


def test_my_function_division_by_zero(capsys) -> None:
    """
    Проверка ошибки деления на "0"
    """
    my_function(4, 0)
    captured = capsys.readouterr()
    assert "my_function error: division by zero. Inputs: (4, 0), {}" in captured.out


@log(filename="test_log.txt")
def my_function_sum(x: float, y: float) -> float:
    return x + y


def test_my_function_file_output() -> None:
    """
    Проверка вывода в файл
    """
    my_function_sum(2, 3)
    with open("test_log.txt", "r", encoding="utf-8") as file:
        content = file.read()
    assert "Функция my_function_sum ок. Результат: 5" in content
    os.remove("test_log.txt")


@log()
def my_function_key_error() -> str:
    return {"a": 1}["b"]


def test_my_function_key_error(capsys) -> None:
    """
    Проверка обработки других исключений
    """
    my_function_key_error()
    captured = capsys.readouterr()
    assert "my_function_key_error error: 'b'. Inputs: (), {}\n" in captured.out


@log()
def my_function_concat(a: float, b: float) -> float:
    return a + b


def test_my_function_concat_strings(capsys) -> None:
    """
    Проверка с разными типами аргументов
    """
    result = my_function_concat("hello", "world")
    assert result == "helloworld"
    captured = capsys.readouterr()
    assert "my_function_concat ок. Результат: helloworld" in captured.out


def test_file_cleanup() -> None:
    """
    Проверка очистки файла
    """
    filename = "test_log_cleanup.txt"

    @log(filename=filename)
    def my_function_cleanup(x):
        return x

    my_function_cleanup(1)
    assert os.path.exists(filename)
    os.remove(filename)
    assert not os.path.exists(filename)
