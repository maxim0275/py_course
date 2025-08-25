# # Определяем путь к файлам
# import os
#
# from src.transaction_importer import reading_operations_from_excel, reading_operations_from_csv
#
# root_dir = os.path.dirname(os.path.abspath(__file__))
# file1_path = os.path.join(root_dir, "data", "transactions_1.csv")
# file2_path = os.path.join(root_dir, "data", "transactions_excel.xlsx")
#
# print(reading_operations_from_excel(file2_path))
# print("================================================================================================")
# print("================================================================================================")
# print("================================================================================================")
# print("================================================================================================")
# print(reading_operations_from_csv(file1_path))

text1 = """
Программа: Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""

print(text1)
answer1 = input("Пользователь: ")

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
while answer3 not in ["EXECUTED", "CANCELED", "PENDING"]:
    print(text3)
    answer3 = input("Пользователь: ")
    if answer3 not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'Программа: Статус операции "{answer3}" недоступен.')

text4 = "Программа: Отсортировать операции по дате? Да/Нет"
answer4 = ""
while answer4 not in ["Да", "Нет"]:
    print(text4)
    answer4 = input("Пользователь: ")
    if answer4 not in ["Да", "Нет"]:
        print(f'Ответ неверный.')

text5 = "Отсортировать по возрастанию или по убыванию? "
answer5 = ""
while answer5 not in ["по возрастанию", "по убыванию"]:
    print(text5)
    answer5 = input("Пользователь: ")
    if answer5 not in ["по возрастанию", "по убыванию"]:
        print(f'Ответ неверный.')

text6 = "Выводить только рублевые транзакции? Да/Нет "
answer6 = ""
while answer6 not in ["Да", "Нет"]:
    print(text6)
    answer6 = input("Пользователь: ")
    if answer6 not in ["Да", "Нет"]:
        print(f'Ответ неверный.')

text7 = "Отфильтровать список транзакций по определенному слову в описании? Да/Нет"
answer7 = ""
while answer7 not in ["Да", "Нет"]:
    print(text7)
    answer7 = input("Пользователь: ")
    if answer7 not in ["Да", "Нет"]:
        print(f'Ответ неверный.')

text8 = "Введите слово для фильтра."
answer8 = input("Пользователь: ")
