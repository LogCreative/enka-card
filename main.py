import asyncio

from enkanetwork import EnkaNetworkAPI, Language

from generator import generate_image
from avatardown import download_avatar

client = EnkaNetworkAPI(lang=Language.CN)
uid = 273518546


async def main():
    async with client:
        data = await client.fetch_user_by_uid(uid)
        for character in data.characters:
            print(f"[{uid}] Generating enka-card for {character.name}")
            download_avatar(character)
            generate_image(data, character, client.lang)


asyncio.run(main())
