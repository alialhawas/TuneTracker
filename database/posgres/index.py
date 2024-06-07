import psycopg2
from psycopg2 import pool

from src.config import conn_params


conn_pool = psycopg2.pool.SimpleConnectionPool(1, 10, **conn_params)


insert_artiest_query = "INSERT INTO artists (artist_id, artist_name, popularity, followers, genre_1, genre_2, genre_3, genre_4, genre_5, image1, image2, image3) VALUES "


def escape_string(value : str) -> str:
    return value.replace("'", "''")

def format_genres(genres: list)-> list:
    """
    this function formats the genres list to have 5 elements if the list has less than 5 elements it will add None to the list
    input: list of genres ex: ['pop', 'rock']
    output: list of 5 genres ex: ['pop', 'rock', None, None, None]
    """
    genres = genres[:5]  
    genres += [None] * (5 - len(genres)) 
    return genres


def format_insert_artiests_Q (artiest_data: list) -> str :

    values = []
    for artist in artiest_data['items']:
        artist_id = artist['id']
        artist_name = escape_string(artist['name'])
        popularity = artist['popularity']
        followers = artist['followers']['total']
        genres = format_genres(artist['genres'])
        image1 = escape_string(artist['images'][0]['url']) if len(artist['images']) > 0 else ''
        image2 = escape_string(artist['images'][1]['url']) if len(artist['images']) > 1 else ''
        image3 = escape_string(artist['images'][2]['url']) if len(artist['images']) > 2 else ''

        values.append(f"('{artist_id}', '{artist_name}', {popularity}, {followers}, "
                    f"'{escape_string(genres[0]) if genres[0] else 'null'}', "
                    f"'{escape_string(genres[1]) if genres[1] else 'null'}', "
                    f"'{escape_string(genres[2]) if genres[2] else 'null'}', "
                    f"'{escape_string(genres[3]) if genres[3] else 'null'}', "
                    f"'{escape_string(genres[4]) if genres[4] else 'null'}', "
                    f"'{image1}', '{image2}', '{image3}')")

    insert_query += ", ".join(values) + ";"

    return insert_query



def execute_query(query, message):
    conn = None
    cur = None
    try:
        conn = conn_pool.getconn()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print(f"{message} successful")
    except Exception as e:
        if conn:
            conn.rollback()  # Rollback in case of error
        print(f"An error occurred: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            # Release the connection back to the pool
            conn_pool.putconn(conn)