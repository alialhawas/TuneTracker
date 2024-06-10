# import asyncio

# import asyncio

# async def fetch_data_1():
#     print("Start fetching data 1...")
#     await asyncio.sleep(2)  # Simulate a network request with a 2-second delay
#     print("Data 1 fetched")
#     return {"data": "sample data 1"}

# async def fetch_data_2():
#     print("Start fetching data 2...")
#     await asyncio.sleep(1)  # Simulate a network request with a 3-second delay
#     print("Data 2 fetched")
#     return {"data": "sample data 2"}

# async def main():
#     task1 = asyncio.create_task(fetch_data_1())
#     task2 = asyncio.create_task(fetch_data_2())

#     # Wait for both tasks to complete
#     results = await asyncio.gather(task1, task2)

#     print(a)
#     print(results)

# # Run the main function
# asyncio.run(main())




def escape_string(value : str) -> str:
    return value.replace("'", "''")



import json

file_path = './mock/apisRes/toptracts.json'

with open(file_path, 'r') as file:
    data = json.load(file)


import json

def format_insert_songs_query(json_data):
    insert_songs_query = "INSERT INTO songs (artist_name, artist_id, release_date, image1, image2, image3, external_url, song_name, popularity, preview_url, song_id) VALUES "

    values = []
    for track in json_data['items']:
        artist_name = escape_string(track['artists'][0]['name'])
        artist_id = track['artists'][0]['id']
        release_date = track['album']['release_date']
        images = track['album']['images']
        image1 = escape_string(images[0]['url']) if len(images) > 0 else ''
        image2 = escape_string(images[1]['url']) if len(images) > 1 else ''
        image3 = escape_string(images[2]['url']) if len(images) > 2 else ''
        external_url = escape_string(track['external_urls']['spotify'])
        song_name = escape_string(track['name'])
        popularity = track['popularity']
        preview_url = escape_string(track['preview_url'])
        song_id = track['id']

        values.append(f"('{artist_name}', '{artist_id}', '{release_date}', '{image1}', '{image2}', '{image3}', '{external_url}', '{song_name}', {popularity}, '{preview_url}', '{song_id}')")

    insert_songs_query += ", ".join(values) + ";"
    return insert_songs_query

# Example usage
json_string = '''
{
  "items": [
    {
      "album": {
        "release_date": "2024-04-19",
        "images": [
          {"url": "https://i.scdn.co/image/ab67616d0000b273e37d133dc75e83b8fb58fbe4"},
          {"url": "https://i.scdn.co/image/ab67616d00001e02e37d133dc75e83b8fb58fbe4"},
          {"url": "https://i.scdn.co/image/ab67616d00004851e37d133dc75e83b8fb58fbe4"}
        ]
      },
      "artists": [
        {
          "id": "6NnBBumbcMYsaPTHFhPtXD",
          "name": "VOILÀ"
        }
      ],
      "external_urls": {
        "spotify": "https://open.spotify.com/track/1cEml7iH5h7cqd8Dn4HzdF"
      },
      "id": "1cEml7iH5h7cqd8Dn4HzdF",
      "name": "Dead To Me",
      "popularity": 54,
      "preview_url": "https://p.scdn.co/mp3-preview/3f6b730e5366c61eb0913ca13248453c4f663261?cid=cfe923b2d660439caf2b557b21f31221"
    },
    {
      "album": {
        "release_date": "2024-04-12",
        "images": [
          {"url": "https://i.scdn.co/image/ab67616d0000b27380d86d636244b72a3a1eede2"},
          {"url": "https://i.scdn.co/image/ab67616d00001e0280d86d636244b72a3a1eede2"},
          {"url": "https://i.scdn.co/image/ab67616d0000485180d86d636244b72a3a1eede2"}
        ]
      },
      "artists": [
        {
          "id": "3y2cIKLjiOlp1Np37WiUdH",
          "name": "Shaboozey"
        }
      ],
      "external_urls": {
        "spotify": "https://open.spotify.com/track/2FQrifJ1N335Ljm3TjTVVf"
      },
      "id": "2FQrifJ1N335Ljm3TjTVVf",
      "name": "A Bar Song (Tipsy)",
      "popularity": 96,
      "preview_url": "https://p.scdn.co/mp3-preview/59f68f3e96233e3c352659053dd48039790cd965?cid=cfe923b2d660439caf2b557b21f31221"
    }
  ]
}
'''

json_data = json.loads(json_string)
extracted_values = format_insert_songs_query(data)


print(extracted_values)

"""
- artiest name 
- artiest id
- release_date
- image1
- image2
- image3
- external_url
- song name
- popularity
- preview_url
- song_id
"""





# print(format_insert_artiests_Q(data)) 