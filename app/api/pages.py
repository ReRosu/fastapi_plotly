from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi import status
import pathlib

pages_router = APIRouter(tags=['pages'])
SITE_DIR: str = str(pathlib.Path(__file__).parent.parent.parent)

@pages_router.get('/')
async def index():
    with open(SITE_DIR+'/site/index.html', 'r') as indexhtml:
        return HTMLResponse(indexhtml.read())