from fastapi import APIRouter,Query
from jiosaavn.Async import song,searchSong

router = APIRouter()

@router.get('/')
async def getSongInfo(
    url:str=Query(None),
    id:str=Query(None),
    query:str=Query(None),
    p:int=Query(1),
    n:int=Query(10),
    lyrics:bool=Query(False)):
    if query:await searchSong(query=query,page=p,limit=n)
    if url:return await song(url=url,lyrics=lyrics)
    if id:return await song(id=id,lyrics=lyrics)
    return {'status':'please provide url or id'}
