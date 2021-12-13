from fastapi import APIRouter,Query
from jiosaavn.Async import song,searchSong

from app.cache import detaCache,expire,log

router = APIRouter()

@router.get('/')
@detaCache.cache(expire,log)
async def getSongInfo(
    url:str=Query(None),
    id:str=Query(None),
    query:str=Query(None),
    p:int=Query(1),
    n:int=Query(10),
    lyrics:bool=Query(False)):
    if url:return await song(url=url,lyrics=lyrics)
    if id:return await song(id=id,lyrics=lyrics)
    if query:return await searchSong(query=query,page=p,limit=n)
    return {'status':'please provide url or id'}
