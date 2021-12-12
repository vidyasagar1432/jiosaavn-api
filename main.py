
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from app.api.api import ApiRouter

description = """
#### JioSaavn API written in Python using [FastAPI](https://github.com/tiangolo/fastapi)
# [Github](https://github.com/vidyasagar1432/jiosaavn-api)
#### **Made using**:
#### [FastAPI](https://github.com/tiangolo/fastapi) is a modern, fast (high-performance), web framework for building APIs
#### [Uvicorn](https://github.com/encode/uvicorn) is a lightning-fast ASGI server implementation,
#### [Pydantic](https://github.com/samuelcolvin/pydantic/) is used for data validation and settings management using python type annotations.
#### [jiosaavn](https://github.com/vidyasagar1432/jiosaavn) is used to Search songs & album. Get song, album, playlist & lyric information from JioSaavn.

"""


app = FastAPI(title='jiosaavn-api', version=1.0,description=description,)

app.include_router(ApiRouter,tags=['Api'])


@app.get("/robots.txt",include_in_schema=False)
async def robots_txt():
    return ''

@app.get("/",include_in_schema=False)
async def root(request: Request):
    return RedirectResponse('/docs')



