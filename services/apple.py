import contextlib
import httpx

from typing import List
from defs import Music

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_2) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.0 Mobile Safari/537.36"}


class Apple:
    @staticmethod
    async def get(keyword: str) -> List[Music]:
        try:
            async with httpx.AsyncClient(headers=headers) as client:
                req = await client.get(f"https://itunes.apple.com/search?term={keyword}&entity=song&limit=4")
                req = req.json()
        except Exception:
            return []
        if req.get("resultCount", 0) == 0:
            return []
        results = []
        for i in req["results"]:
            with contextlib.suppress(Exception):
                results.append(Music(i["trackName"], i["artworkUrl100"]))
        return results
