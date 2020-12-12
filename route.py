from data_base import anime_data

def get_all():
    return anime_data()

def get_name(name):
    for item in anime_data():
        if name in item["name"]:
            return item
    else:
        return None

def get_genres(gen):
    data = []
    for item in anime_data():
        if gen in item["geresn"]:
            data.append(item)
    return data
