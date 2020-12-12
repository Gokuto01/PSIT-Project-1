import pandas as pd 
#https://stackoverflow.com/questions/2974022/is-it-possible-to-assign-the-same-value-to-multiple-keys-in-a-dict-object-at-onc
sheet_id = '1XTmcMfTa9BLlqXfhvE4wDN0lkMaLkkzP809vb4FLKpw'
df  = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')

def  multi_key_dict_get(d, k):
    for keys, v in d.items():
        if k in keys:
            return v
    return None

def anime_dict():
    name_link_anime = {}
    num_anime = list(df.get('NO.'))[-1]
    for i in range(num_anime):
        str_name = df.get('NAME')[i]
        tuple_name = tuple(str_name.split(', '))
        link_name = df.get('LINK')[i]
        name_link_anime.update({tuple_name: link_name})
    return name_link_anime
