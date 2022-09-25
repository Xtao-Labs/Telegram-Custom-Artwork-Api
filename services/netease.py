import contextlib

from typing import List
from pyncm import GetCurrentSession, apis
from defs import Music


class Netease:
    @staticmethod
    async def get(keyword: str) -> List[Music]:
        # 海外用户
        GetCurrentSession().headers["X-Real-IP"] = "118.88.88.88"
        try:
            req = apis.cloudsearch.GetSearchResult(keyword)
            songs = req["result"]["songs"]
        except Exception:
            return []
        results = []
        for i in songs:
            with contextlib.suppress(Exception):
                results.append(Music(i["name"], i["al"]["picUrl"].replace("http:", "https:")))
        return results
