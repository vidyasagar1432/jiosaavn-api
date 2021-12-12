from fastapi import APIRouter,Query
from jiosaavn.Async import song,searchSong

router = APIRouter()

@router.get('/')
async def getSongInfo(
    url:str=Query(None),
    id:str=Query('veJXEDAz'),
    query:str=Query(None),
    p:int=Query(1),
    n:int=Query(10),
    lyrics:bool=Query(False)
    ):
    'Get song detail from url or id'
    if query:
        await searchSong(query=query,page=p,limit=n)
    return await song(url=url,id=id,lyrics=lyrics)

# @router.get('/search')
# async def search(query:str=Query(...),p:int=Query(1),n:int=Query(10)):
#     'Search song from query'
#     return await searchSong(query=query,page=p,limit=n)


# @router.get('/lyrics')
# async def getLyricsInfo(url:str=Query(None),id:str=Query('veJXEDAz')):
#     'Get lyrics of a song from url or id (If Available)'
#     return await lyrics(url=url,id=id)