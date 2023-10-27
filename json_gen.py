import os
import json

# Function to generate a JSON file for artists
def generate_artist_json(MUSIC_DIR):
    artists = os.listdir(MUSIC_DIR)
    artist_data = [{'name': artist} for artist in artists]
    with open(f'{MUSIC_DIR}/{CAL_DIR}/meta/artists.json', 'w') as file:  # Save in the "music_index" folder
        json.dump(artist_data, file)

# Function to generate a JSON file for albums of a specific artist
def generate_album_json(artist, MUSIC_DIR):
    artist_dir = os.path.join(MUSIC_DIR, artist)

    if not os.path.isdir(artist_dir):
        return  # Artist directory not found

    albums = sorted([item for item in os.listdir(artist_dir) if os.path.isdir(os.path.join(artist_dir, item))])
    album_data = [{'name': album} for album in albums]
    with open(f'{MUSIC_DIR}/{CAL_DIR}/albums/{artist}_albums.json', 'w') as file:  # Save in the "music_index" folder
        json.dump(album_data, file)

# Function to generate a JSON file for songs of a specific album
def generate_songs_json(artist, album, MUSIC_DIR):
    artist_dir = os.path.join(MUSIC_DIR, artist)
    album_dir = os.path.join(artist_dir, album)

    if not os.path.isdir(album_dir):
        return  # Album directory not found

    songs = sorted(os.listdir(album_dir))
    song_data = [{'name': song} for song in songs]
    with open(f'{MUSIC_DIR}/{CAL_DIR}/songs/{artist}_{album}_songs.json', 'w') as file:  # Save in the "music_index" folder
        json.dump(song_data, file)