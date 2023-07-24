import asyncio

from enkanetwork import EnkaNetworkAPI, Language

from generator import generate_image
from avatardown import download_avatar
from webgen import generate_webpage

client = EnkaNetworkAPI(lang=Language.CN)
uid = 273518546


async def main():
    async with client:
        data = await client.fetch_user_by_uid(uid)
        for character in data.characters:
            print(f"[{uid}] Generating enka-card for {character.name}")
            download_avatar(character)
            generate_image(data, character, client.lang)
        generate_webpage(data.characters)
        print(f"[{uid}] Web page is generated in genshin.html and genshin_config.js")


asyncio.run(main())
