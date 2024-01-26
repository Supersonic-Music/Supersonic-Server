#!/usr/bin/python

from flask import Flask, send_file, render_template, abort, jsonify
from flask_cors import CORS
from colorama import Fore
from info import ProgramData
from lightyear import generate_lightyear_stats

ProgramData = ProgramData()
from config.config import UserOptions

UserOptions = UserOptions()
import urllib.parse, os, socket, time

app = Flask(__name__)
CORS(app)

MUSIC_DIR = UserOptions.MUSIC_DIR
CAL_DIR = UserOptions.CAL_DIR

app.config["SECRET_KEY"] = "rubrub123"


@app.route("/music/<path:filename>")
def serve_music(filename):
    music_file = os.path.join(MUSIC_DIR, filename)

    if not os.path.isfile(music_file):
        return abort(404)  # File not found
    print("User listened to " + music_file)
    if music_file.rsplit(".", 1)[1] in UserOptions.MUSIC_FILETYPES:
        with open(UserOptions.LIGHTYEAR_PATH, "a") as song_log:
            song_log.write(filename + "\n")
    return send_file(music_file)


@app.route("/")
def index():
    artists = os.listdir(MUSIC_DIR)
    PROGRAM_NAME = ProgramData.PROGRAM_NAME
    return render_template(
        "index.html",
        artists=artists,
        PROGRAM_NAME=PROGRAM_NAME,
        number_of_artists=stats["number_of_artists"],
        number_of_albums=stats["number_of_albums"],
        number_of_songs=stats["number_of_songs"],
        lightyear_songs_listened_to=lightyear_stats[0][0]["songs_listened_to"],
        lightyear_artists_listened_to=lightyear_stats[0][0]["artists_listened_to"],
        lightyear_albums_listened_to=lightyear_stats[0][0]["albums_listened_to"],
        lightyear_artists=lightyear_stats[1],
    )


@app.route("/<artist>/")
def artist_albums(artist):
    artist_dir = os.path.join(MUSIC_DIR, artist)

    if not os.path.isdir(artist_dir):
        return abort(404)  # Artist directory not found

    albums = sorted(
        [
            item
            for item in os.listdir(artist_dir)
            if os.path.isdir(os.path.join(artist_dir, item))
        ]
    )
    return render_template("artist_albums.html", artist=artist, albums=albums)


@app.route("/lightyear/")
def lightyear():
    PROGRAM_NAME = ProgramData.PROGRAM_NAME
    print(lightyear_stats)
    return render_template(
        "lightyear.html",
        PROGRAM_NAME=PROGRAM_NAME,
        songs_listened_to=lightyear_stats[0][0]["songs_listened_to"],
        albums_listened_to=lightyear_stats[0][0]["albums_listened_to"],
        artists_listened_to=lightyear_stats[0][0]["artists_listened_to"],
        artists=lightyear_stats[1],
    )


@app.route("/<artist>/<album>/")
def album_songs(artist, album):
    artist_dir = os.path.join(MUSIC_DIR, artist)
    album_dir = os.path.join(artist_dir, album)

    if not os.path.isdir(album_dir):
        return abort(404)  # Album directory not found

    songs = sorted(os.listdir(album_dir))
    return render_template("album.html", artist=artist, album=album, songs=songs)


if __name__ == "__main__":
    if UserOptions.SCAN_COLLECTION_ON_STARTUP == True:
        from scan_music import scan_music

        start_time = time.time()
        stats = scan_music(MUSIC_DIR, CAL_DIR)
        end_time = time.time()
        time_taken = str(round(end_time - start_time, 2))
        if time_taken.endswith(".0"):
            time_taken = time_taken[:-2]
        print(f"✅ Scanned music collection in {time_taken} seconds.")
        lightyear_stats = generate_lightyear_stats(UserOptions.LIGHTYEAR_PATH)
    from waitress import serve

    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print(
        f"🌐 Visit the Web Management Interface at:\n➡️ {Fore.LIGHTBLUE_EX}{UserOptions.protocol}://{Fore.WHITE}localhost{Fore.LIGHTBLUE_EX}:6969\n➡️ {UserOptions.protocol}://{Fore.WHITE}{IPAddr}{Fore.LIGHTBLUE_EX}:6969"
    )
    serve(app=app, host="0.0.0.0", port=6969)
