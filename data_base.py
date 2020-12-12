import pandas as pd 

sheet_id = '1XTmcMfTa9BLlqXfhvE4wDN0lkMaLkkzP809vb4FLKpw'
df  = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')

def anime_data():
    data=[]
    num_anime = list(df.get('NO.'))[-1]
    for i in range(num_anime):
        anime = {}
        anime['name'] = tuple(df.get("NAME")[i].split(', '))
        anime['link'] = df.get("LINK")[i]
        anime['genres'] = tuple(df.get("GENRES")[i].split(', '))
        anime['id'] = str(df.get("NO.")[i])
        data.append(anime)
    return data
