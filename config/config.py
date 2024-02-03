from dataclasses import dataclass
from os import path
from info import ProgramData

ProgramData = ProgramData()
import subprocess


# Choose your desired options below.
@dataclass
class UserOptions:
    protocol = "http"
    newlines = "\n"
    MUSIC_DIR = "C:/Users/ethan/Music"
    # MUSIC_DIR = "path/to/your/music" # This must be the directory above all your artists.
    CAL_DIR = ".cal"
    LIGHTYEAR_PATH = path.join(MUSIC_DIR, CAL_DIR, "meta", "lightyear.txt")
    PLAYLIST_EXTENSION = ".tardis"
    SCAN_COLLECTION_ON_STARTUP = True

    # Formatting Options
    AUTO_REMOVE_UTC_TIMESTAMP = (
        True  # Automatically remove UTC timestamps from the end of song names
    )
    IGNORE_THUMBS_DB = True  # Ignore Windows Thumbnail Database files.
    IGNORE_DESKTOP_INI = True  # Ignore Windows Desktop.ini files.

    IGNORED_FILES = [
            'Thumbs.db', 
            'desktop.ini', 
    ]

    # Filetype Options
    MUSIC_FILETYPES = [
        "mp3",
        "flac",
        "ogg",
        "m4a",
        "wav",
        "wma",
        "aac",
        "aiff",
        "alac",
        "dsd",
        "dsf",
        "dff",
        "ape",
        "opus",
        "mka",
        "mpc",
        "mp+",
        "mpp",
    ]
