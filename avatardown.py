from enkanetwork.model.character import CharacterInfo
from utils import check_asset, get_output_dir
import shutil

def download_avatar(character: CharacterInfo):
    cache_path = f"attributes/Genshin/Avatar/{character.image.icon.filename}.png"
    check_asset(path=cache_path,
                asset_url=character.image.icon.url)
    shutil.copyfile(src=cache_path,
                    dst=f"{get_output_dir()}/{character.name}_icon.png")
