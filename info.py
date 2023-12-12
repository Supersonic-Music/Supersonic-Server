from dataclasses import dataclass


@dataclass
class ProgramData:
    PROGRAM_NAME: str = "Supersonic Server"
    PROGRAM_VERSION: str = "0.idk"
    auto_user_music = f"/home/{subprocess.check_output('echo $USER', shell=True, text=True).strip(newlines)}/Music/"
