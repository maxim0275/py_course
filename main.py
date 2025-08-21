from src.external_api import get_summ_rated
from src.utils import get_fin_data, get_summ_trans

# path_to_file = "data//operations.json"
path_to_file = "data//operations.json"
tr = get_fin_data(path_to_file)

print(tr[70])


sm = get_summ_trans(tr[74])
print(sm)

print(get_summ_rated("USe", 1))



# from src.masks import get_mask_card_number, get_mask_account
#
# print(get_mask_card_number("7000179289606361"))
# print(get_mask_account("73654108140358743015"))