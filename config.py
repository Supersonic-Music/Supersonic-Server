from dataclasses import dataclass
from os import path
import subprocess

# Choose your desired options below.
@dataclass
class UserOptions: 
    newlines = "\n"
    MUSIC_DIR = f"/home/{subprocess.check_output('echo $USER', shell=True, text=True).strip(newlines)}/Music/"
    CAL_DIR = ".cal"
    LIGHTYEAR_PATH = path.join(MUSIC_DIR, CAL_DIR, "meta", "lightyear.txt")
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
