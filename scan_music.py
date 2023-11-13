import json_gen, json, os
from config import UserOptions
UserOptions = UserOptions()

def scan_music(MUSIC_DIR, CAL_DIR):
    # Generate the JSON data for artists
    json_gen.generate_artist_json(MUSIC_DIR, CAL_DIR)
    print(MUSIC_DIR)
    print(CAL_DIR)

    # Read the artists' JSON data into a Python list
    with open(os.path.join(MUSIC_DIR, CAL_DIR, 'meta', 'artists.json'), 'r') as file:
        artists_data = json.load(file)
    
    # Extract the artist names from the JSON data and create a list
    list_of_artists = [artist['name'] for artist in artists_data]
    utc_removed_fr = 0
    for artist in list_of_artists:
        # Generate the JSON data for albums of each artist
        json_gen.generate_album_json(artist, MUSIC_DIR, CAL_DIR)

        # Read the albums' JSON data into a Python list
        with open(os.path.join(MUSIC_DIR, CAL_DIR, 'albums', f'{artist}_albums.json'), 'r') as album_file:
            albums_data = json.load(album_file)

        # Extract the album names from the JSON data
        list_of_albums = [album['name'] for album in albums_data]
        for album in list_of_albums:
            # Generate the JSON data for songs of each album
            utc_removed_fr += json_gen.generate_songs_json(artist, album, MUSIC_DIR, CAL_DIR)
    print(f"Removed UTC timestamps from {utc_removed_fr} songs. This behaviour can be disabled in config.py.")

print("SCANNING MUSIC")
MUSIC_DIR = UserOptions.MUSIC_DIR
CAL_DIR = UserOptions.CAL_DIR