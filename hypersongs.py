import os, tomllib


def is_in_hypersongs(hypersongs, artist, album):
    for song in hypersongs["songs"]:
        if (
            hypersongs["songs"][song]["artist"] == artist
            and hypersongs["songs"][song]["album"] == album
        ):
            return True


def generate_hypersongs_json(hypersongs):
    hypersongs_json = []
    for song in hypersongs["songs"]:
        hypersongs_json.append(
            {
                "artist": hypersongs["songs"][song]["artist"],
                "album": hypersongs["songs"][song]["album"],
                "song": hypersongs["songs"][song]["song"],
            }
        )


with open(os.path.join("config", "hypersongs.toml"), "rb") as hypersongs_file:
    hypersongs = tomllib.load(hypersongs_file)

generate_hypersongs_json(hypersongs)
