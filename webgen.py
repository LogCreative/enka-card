from enkanetwork.model.character import CharacterInfo
import shutil
from utils import get_output_dir

def generate_webpage(characters: list[CharacterInfo]):
    characters_name = []
    for character in characters:
        characters_name.append(f'"{character.name}"')
    with open(f"{get_output_dir()}/genshin_config.js", "w") as config_file:
        config_file.write(f"characters = [{', '.join(characters_name)}]\nrootdir = \".\"")
    shutil.copy(src='attributes/Templates/genshin.html',dst=f"{get_output_dir()}/genshin.html")
