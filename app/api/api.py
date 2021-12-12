from fastapi import APIRouter
from app.api.routes import songs,albums,playlists,lyrics


ApiRouter = APIRouter()


ApiRouter.include_router(songs.router,prefix='/songs')
ApiRouter.include_router(albums.router,prefix='/albums')
ApiRouter.include_router(playlists.router,prefix='/playlists')
ApiRouter.include_router(lyrics.router,prefix='/lyrics')