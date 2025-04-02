from fastapi import FastAPI, Query
from starlette.responses import RedirectResponse

from utils import get_music

app = FastAPI()


@app.get('/search')
async def search(
    *,
    service: str = "apple",
    keyword: str = Query(..., title="The name of a song")
):
    return await get_music(service, keyword)


@app.get("/")
async def root():
    return RedirectResponse(url="https://music.163.com", status_code=302)


@app.get("/favicon.ico")
async def root2():
    return RedirectResponse(url="https://s1.music.126.net/style/favicon.ico", status_code=302)
