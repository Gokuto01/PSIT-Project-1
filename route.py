from data_base import anime_data

def get_all():
    return anime_data()

def get_name(name):
    return (item for item in anime_data() if name in dict_items["name"])

def select_type(types):
    return (item for item in anime_data() if types in dict_items["type"])

def link_anime(link):
    return (item for item in anime_data() if link in dict_items["link"])

def return_all(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    return row
