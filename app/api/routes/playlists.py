from fastapi import APIRouter,Query
from jiosaavn.Async import playlist

router = APIRouter()

@router.get('/')
async def getPlaylistInfo(url:str=Query(None),id:str=Query(None),lyrics:bool=Query(False)):
    'Get playlist information from url or id'
    if url:return await playlist(url=url,lyrics=lyrics)
    if id:return await playlist(id=id,lyrics=lyrics)
    return {'status':'please provide url or id'}

