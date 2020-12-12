from data_base import anime_data

def get_all():
    return anime_data()

def get_name(name):
    for item in anime_data():
        if name in item["name"]:
            return item
    else:
        return None

def get_genres(genres):
    data=[]
    for item in anime_data():
        if genres in item["genres"]:
            data.append(item)
    return data
