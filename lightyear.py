import os
from config.config import UserOptions
from mutagen.mp3 import MP3

UserOptions = UserOptions()


def get_song_length(filename):
    filename = os.path.join(UserOptions.MUSIC_DIR, filename)
    filename = filename.strip()  # Remove leading and trailing whitespace
    print(filename)
    audio = MP3(filename)
    audio_length_in_minutes = round(audio.info.length / 60)
    return audio_length_in_minutes


def generate_lightyear_stats(LIGHTYEAR_PATH):
    if os.path.isfile(LIGHTYEAR_PATH):
        with open(LIGHTYEAR_PATH, "r") as song_log:
            songs = song_log.readlines()
    else:
        songs = []
    stats = [
        [
            {
                "songs_listened_to": len(songs),
                "artists_listened_to": len(set([song.split("/")[0] for song in songs])),
                "albums_listened_to": len(set([song.split("/")[1] for song in songs])),
            }
        ]
    ]
    artists = []
    for song in songs:
        if os.path.isdir(song):
            artist = song.split("/")[0]
            if artist not in [artist["artist"] for artist in artists]:
                artist_songs = [song for song in songs if song.split("/")[0] == artist]
                total_minutes_listened = sum(
                    [get_song_length(song) for song in artist_songs]
                )
                artist_data = {
                    "artist": artist,
                    "number_of_times_artist_listened_to": len(artist_songs),
                    "albums_listened_to": len(
                        set([song.split("/")[1] for song in artist_songs])
                    ),
                    "songs_listened_to": len(artist_songs),
                    "total_minutes_listened": total_minutes_listened,
                }
                artists.append(artist_data)
    stats.append(artists)
    print(
        f"🎧 You have listened to {stats[0][0]['songs_listened_to']} songs by {stats[0][0]['artists_listened_to']} artists from {stats[0][0]['albums_listened_to']} albums."
    )
    print("")
    for artist in artists:
        print(
            f"You have listened to {artist['number_of_times_artist_listened_to']} songs by {artist['artist']} from {artist['albums_listened_to']} albums for ~{artist['total_minutes_listened']} minutes in total."
        )
    return stats
