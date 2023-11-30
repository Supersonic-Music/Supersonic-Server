from dataclasses import dataclass

# Choose your desired options below.
@dataclass
class UserOptions:
    MUSIC_DIR = "/home/deck/Music/"
    CAL_DIR = ".cal"
    LIGHTYEAR_PATH = "lightyear.txt"
    PLAYLIST_EXTENSION = ".tardis"
    SCAN_COLLECTION_ON_STARTUP = True
    
    # Formatting Options
    AUTO_REMOVE_UTC_TIMESTAMP = True

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