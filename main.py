from src.external_api import get_summ_rated
from src.utils import get_fin_data, get_summ_trans

# path_to_file = "data//operations.json"
path_to_file = "data//operations.json"
tr = get_fin_data(path_to_file)

print(tr[74])

sm = get_summ_trans(tr[95])
print(sm)

print(get_summ_rated("USe", 1))
