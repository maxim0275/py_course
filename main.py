# Определяем путь к файлам
import os

from src.transaction_importer import reading_operations_from_excel, reading_operations_from_csv

root_dir = os.path.dirname(os.path.abspath(__file__))
file1_path = os.path.join(root_dir, "data", "transactions_1.csv")
file2_path = os.path.join(root_dir, "data", "transactions_excel.xlsx")

# print(reading_operations_from_excel(file2_path))
print("================================================================================================")
print("================================================================================================")
print("================================================================================================")
print("================================================================================================")
print(reading_operations_from_csv(file1_path))
