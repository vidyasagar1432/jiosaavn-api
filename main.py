
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from app.api.api import ApiRouter

description = """
#### JioSaavn API written in Python using [FastAPI](https://github.com/tiangolo/fastapi)

[Github](https://jiosaavn.deta.dev/)

"""


app = FastAPI(title='jiosaavn-api', version=1.0,
        description=description,
        )

app.include_router(ApiRouter,tags=['Api'])


@app.get("/robots.txt",include_in_schema=False)
async def robots_txt():
    return ''

@app.get("/",include_in_schema=False)
async def root(request: Request):
    return RedirectResponse('/docs')



