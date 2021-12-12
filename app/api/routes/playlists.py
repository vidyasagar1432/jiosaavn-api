from fastapi import APIRouter,Query
from jiosaavn.Async import playlist

router = APIRouter()

@router.get('/')
async def getPlaylistInfo(url:str=Query(None),id:str=Query('10496527'),lyrics:bool=Query(False)):
    'Get playlist information from url or id'
    return await playlist(url=url,id=id,lyrics=lyrics)

