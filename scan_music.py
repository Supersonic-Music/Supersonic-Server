import json_gen, json, os, shutil, tomllib
from config.config import UserOptions

UserOptions = UserOptions()


def scan_music(MUSIC_DIR, CAL_DIR):
    with open(os.path.join("config", "hypersongs.toml"), "rb") as hypersongs_file:
        hypersongs = tomllib.load(hypersongs_file)
    # see if the CAL_DIR exists, if not, create it. If it does then delete it and then create it
    if os.path.isdir(os.path.join(MUSIC_DIR, CAL_DIR)):
        if os.path.isdir(os.path.join(MUSIC_DIR, CAL_DIR, "albums")):
            shutil.rmtree(os.path.join(MUSIC_DIR, CAL_DIR, "albums"))
        if os.path.isdir(os.path.join(MUSIC_DIR, CAL_DIR, "songs")):
            shutil.rmtree(os.path.join(MUSIC_DIR, CAL_DIR, "songs"))
    else:
        os.mkdir(os.path.join(MUSIC_DIR, CAL_DIR))
        os.mkdir(os.path.join(MUSIC_DIR, CAL_DIR, "meta"))
    os.mkdir(os.path.join(MUSIC_DIR, CAL_DIR, "albums"))
    os.mkdir(os.path.join(MUSIC_DIR, CAL_DIR, "songs"))

    # Generate the JSON data for artists
    number_of_artists = json_gen.generate_artist_json(MUSIC_DIR, CAL_DIR)

    # Read the artists' JSON data into a Python list
    with open(os.path.join(MUSIC_DIR, CAL_DIR, "meta", "artists.json"), "r") as file:
        artists_data = json.load(file)

    # Extract the artist names from the JSON data and create a list
    list_of_artists = [artist["name"] for artist in artists_data]
    utc_removed_fr = 0
    number_of_albums = 0
    number_of_songs = 0
    all_albums = []
    for artist in list_of_artists:
        # Generate the JSON data for albums of each artist
        album_data = json_gen.generate_album_json(artist, MUSIC_DIR, CAL_DIR)
        all_albums.append(album_data)
        # Read the albums' JSON data into a Python list
        with open(
            os.path.join(MUSIC_DIR, CAL_DIR, "albums", f"{artist}_albums.json"), "r"
        ) as album_file:
            albums_data = json.load(album_file)

        # Extract the album names from the JSON data
        list_of_albums = [album["name"] for album in albums_data]
        for album in list_of_albums:
            number_of_albums += 1
            # Generate the JSON data for songs of each album
            thing = json_gen.generate_songs_json(
                artist, album, MUSIC_DIR, CAL_DIR, number_of_songs
            )
            utc_removed_fr += thing[0]
            number_of_songs = thing[1]
    with open(
        os.path.join(MUSIC_DIR, CAL_DIR, "meta", "albums.json"), "w"
    ) as albums_meta_file:
        json.dump(all_albums, albums_meta_file)
    print(f"✅ Found {number_of_albums} Albums. 💿")
    print(f"✅ Found {number_of_songs} Songs. 🎵")
    print(
        f"✅ Removed UTC timestamps from {utc_removed_fr} songs. 🕒 This behaviour can be disabled in config.py."
    )
    print(f"✅ Finished Scanning {MUSIC_DIR}. 🎉")
    stats = {
        "number_of_artists": number_of_artists,
        "number_of_albums": number_of_albums,
        "number_of_songs": number_of_songs,
    }
    return stats


MUSIC_DIR = UserOptions.MUSIC_DIR
CAL_DIR = UserOptions.CAL_DIR
print(f"Scanning Music in {MUSIC_DIR}.")
