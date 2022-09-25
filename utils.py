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


async def get_music(service: str, keyword: str) -> dict:
    if not keyword:
        return default_data
    with contextlib.suppress(Exception):
        apple_result = await apple.Apple.get(keyword)
        if service == "apple":
            if apple_result:
                return parse_data(apple_result)
            netease_result = await netease.Netease.get(keyword)
            if netease_result:
                return parse_data(netease_result)
        else:
            if apple_result and apple_result[0].name == keyword:
                return parse_data(apple_result)
            netease_result = await netease.Netease.get(keyword)
            if netease_result:
                return parse_data(netease_result)
            if apple_result:
                return parse_data(apple_result)
    return default_data
