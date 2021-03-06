from fastapi import APIRouter,Query
from jiosaavn.Async import lyrics

from app.cache import detaCache,expire,log

router = APIRouter()

@router.get('/')
@detaCache.cache(expire,log)
async def getLyricsInfo(url:str=Query(None),id:str=Query(None)):
    'Get lyrics of a song from url or id (If Available)'
    if url:return await lyrics(url=url)
    if id:return await lyrics(id=id)
    return {'status':'please provide url or id'}