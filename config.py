from dataclasses import dataclass

# Choose your desired options below.
@dataclass
class UserOptions:
    MUSIC_DIR = "/home/ethan/Music"
    CAL_DIR = ".cal_sonic_library"
    PLAYLIST_EXTENSION = ".tardis"
    SCAN_COLLECTION_ON_STARTUP = True
    
    # Formatting Options
    AUTO_REMOVE_UTC_TIMESTAMP = True
