from dataclasses import dataclass

# Choose your desired options below.
@dataclass
class UserOptions:
    MUSIC_DIR = "/home/deck/git/sonic-website/music"
    CAL_DIR = ".cal"
    PLAYLIST_EXTENSION = ".tardis"
    SCAN_COLLECTION_ON_STARTUP = True
    
    # Formatting Options
    AUTO_REMOVE_UTC_TIMESTAMP = True
