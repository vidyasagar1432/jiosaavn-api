from fastapi import APIRouter,Query
from jiosaavn.Async import album,searchAlbum

router = APIRouter()

@router.get('/')
async def getAlbumInfo(
    url:str=Query(None),
    id:str=Query('10496527'),
    query:str=Query(None),
    lyrics:bool=Query(False)):
    'Get Album information from url or id'
    if query:
        return await searchAlbum(query=query)
    return await album(url=url,id=id,lyrics=lyrics)

# @router.get('/search')
# async def albumsearch(query:str=Query(...)):
#     'Search albums from query'
#     return await searchAlbum(query=query)

