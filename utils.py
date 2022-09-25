import contextlib
from typing import List

from defs import Music
from services import apple, netease

default_data = {"resultCount": 0, "results": []}


def parse_data(data: List[Music]) -> dict:
    length = len(data)
    if length == 0:
        return default_data
    results = [{"trackName": i.name, "artworkUrl100": i.album} for i in data]
    return {"resultCount": length, "results": results}


async def get_music(keyword: str) -> dict:
    if not keyword:
        return default_data
    with contextlib.suppress(Exception):
        apple_result = await apple.Apple.get(keyword)
        if apple_result:
            return parse_data(apple_result)
        netease_result = await netease.Netease.get(keyword)
        if netease_result:
            return parse_data(netease_result)
    return default_data
