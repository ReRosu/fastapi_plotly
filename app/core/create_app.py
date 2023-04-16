from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.pages import pages_router

from app.api.v1 import api_v1_router
from app.core.misc import settings


def create_app() -> FastAPI:

    app = FastAPI(title=settings.app_title)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    app.include_router(api_v1_router, prefix=settings.api_prefix)
    app.include_router(pages_router)

    return app
