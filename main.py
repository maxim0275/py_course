from src.utils import get_fin_data

# path_to_file = "data//operations.json"
path_to_file = "data//tr1"
tr = get_fin_data(path_to_file)
print(tr)