from fastapi import FastAPI, Query
from utils import get_music

app = FastAPI()


@app.get('/search')
async def search(
    *,
    keyword: str = Query(..., title="The name of a song")
):
    return await get_music(keyword)
