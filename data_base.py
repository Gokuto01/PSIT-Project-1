import pandas as pd 

sheet_id = '1XTmcMfTa9BLlqXfhvE4wDN0lkMaLkkzP809vb4FLKpw'
dbf = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')

def  multi_key_dict_get(d, k):
    for keys, v in d.items():
        if k in keys:
            return v
    return None

anime_dict = {}
for anime_all in range(50):
    str_name = dbf.get('Name')[i]
    tuple_name = tuple(str_name.split(', '))
    link_name = dbf.get('Link')[i]
    anime_dict.update({tuple_name: link_name})
print(anime_dict)
