import pandas as pd 
#https://stackoverflow.com/questions/2974022/is-it-possible-to-assign-the-same-value-to-multiple-keys-in-a-dict-object-at-onc
sheet_id = '1XTmcMfTa9BLlqXfhvE4wDN0lkMaLkkzP809vb4FLKpw'
dbf = pd.read_csv(f'https://docs.google.com/spreadsheets/d/%7Bsheet_id%7D/export?format=csv%27)

def  multi_key_dict_get(d, k):
    for keys, v in d.items():
        if k in keys:
            return v
    return None

anime_dict = {}
for i in range(50):
    str_name = dbf.get('NAME')[i]
    tuple_name = tuple(str_name.split(', '))
    link_name = dbf.get('LINK')[i]
    anime_dict.update({tuple_name: link_name})
