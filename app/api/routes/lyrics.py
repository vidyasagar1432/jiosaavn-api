from fastapi import APIRouter,Query
from jiosaavn.Async import lyrics

router = APIRouter()

@router.get('/')
async def getLyricsInfo(url:str=Query(None),id:str=Query('veJXEDAz')):
    'Get lyrics of a song from url or id (If Available)'
    return await lyrics(url=url,id=id)