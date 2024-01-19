import os, json, config.config as config

# Function to generate a JSON file for artists
def generate_artist_json(MUSIC_DIR, CAL_DIR):
    artists = os.listdir(MUSIC_DIR)
    artists.sort()
    plugins = []
    artist_data = []
    for artist in artists:
        artist_data.append({'name': artist})  # Corrected line
        if artist.startswith('.') or artist.endswith('.sonic'):
            plugins.append(artist)
        if artist == "Playlists":
            found_playlists = True
        else:
            found_playlists = False
    start_of_list_ish = 0
    for plugin in plugins:
        artist_data.remove({'name': plugin})
        artist_data.insert(start_of_list_ish, {'name': plugin})
        start_of_list_ish += 1
    if found_playlists:
        artist_data.remove({'name': "Playlists"})
        artist_data.insert(start_of_list_ish, {'name': "Playlists"})
        start_of_list_ish += 1
    print(f"✅ Found {len(artist_data)} Artists. 🧑‍🎨") # Found number of artists
    with open(os.path.join(MUSIC_DIR, CAL_DIR, 'meta', 'artists.json'), 'w') as file:  # Save in the "music_index" folder
        json.dump(artist_data, file)
    return len(artist_data)

# Function to generate a JSON file for albums of a specific artist
def generate_album_json(artist, MUSIC_DIR, CAL_DIR):
    artist_dir = os.path.join(MUSIC_DIR, artist)

    if not os.path.isdir(artist_dir):
        return  # Artist directory not found

    albums = sorted([item for item in os.listdir(artist_dir) if os.path.isdir(os.path.join(artist_dir, item))])
    # album_data = [{'name': album} for album in albums
    album_data = []
    album_data_for_meta = []
    album_data_for_meta.append({'artist': artist})
    for album in albums:
        album_dir = os.path.join(artist_dir, album)
        album_data.append({'name': album})
        album_data_for_meta.append({'name': album})
    with open(os.path.join(MUSIC_DIR, CAL_DIR, 'albums', f'{artist}_albums.json'), 'w') as file:  # Save in the "music_index" folder
        json.dump(album_data, file)
    return album_data_for_meta

# Function to generate a JSON file for songs of a specific album
def generate_songs_json(artist, album, MUSIC_DIR, CAL_DIR, number_of_songs):
    artist_dir = os.path.join(MUSIC_DIR, artist)
    album_dir = os.path.join(artist_dir, album)

    if not os.path.isdir(album_dir):
        return  # Album directory not found

    songs = sorted(os.listdir(album_dir))
    song_data = []
    utc_removed = 0
    for song in songs:
        number_of_songs += 1
        if song.startswith("desktop") and song.endswith(".ini"):
            pass
        elif song.startswith("Thumbs") and song.endswith(".db"):
            pass
        else:
            name = song.rsplit(".", 1)[0]
            if name.endswith(" UTC)") and config.UserOptions.AUTO_REMOVE_UTC_TIMESTAMP:
                name = name.rsplit(' (', -1)[0]
                utc_removed += 1
            song_data.append({'name': name, 'path': song})
    with open(os.path.join(MUSIC_DIR, CAL_DIR, 'songs', f'{artist}_{album}_songs.json'), 'w') as file:  # Save in the "music_index" folder
        json.dump(song_data, file)
    song_stats = [utc_removed, number_of_songs]
    return song_stats
