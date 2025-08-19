from src.utils import get_fin_data, get_summ_trans

# path_to_file = "data//operations.json"
path_to_file = "data//operations.json"
tr = get_fin_data(path_to_file)

print(tr[74])

sm = get_summ_trans(tr[95])
print(sm)

# count = 0
# for tr1 in tr:
#     count = count + 1
#     sm = get_summ_trans(tr1)
#     print(count, sm)
