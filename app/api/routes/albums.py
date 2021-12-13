from fastapi import APIRouter,Query
from jiosaavn.Async import album,searchAlbum

from app.cache import detaCache,expire,log

router = APIRouter()

@router.get('/')
@detaCache.cache(expire,log)
async def getAlbumInfo(
    url:str=Query(None),
    id:str=Query(None),
    query:str=Query(None),
    lyrics:bool=Query(False)):
    if query:return await searchAlbum(query=query)
    if url:return await album(url=url,lyrics=lyrics)
    if id:return await album(id=id,lyrics=lyrics)
    return {'status':'please provide url or id'}


