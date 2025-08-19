from src.utils import get_fin_data, get_summ_trans

# path_to_file = "data//operations.json"
path_to_file = "data//operations.json"
tr = get_fin_data(path_to_file)

print(tr[1])
sm = get_summ_trans(tr[1])
print(sm)
