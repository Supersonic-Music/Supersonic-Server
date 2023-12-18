from dataclasses import dataclass
import pwd, os


@dataclass
class ProgramData:
    PROGRAM_NAME: str = "Supersonic Server"
    PROGRAM_VERSION: str = "0.idk"
    auto_user_music = f"/home/{pwd.getpwuid(os.getuid())[0]}/Music"
