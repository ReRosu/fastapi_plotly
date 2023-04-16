import os
import pathlib

from pydantic import BaseSettings

BASE_DIR: str = str(pathlib.Path(__file__).parent.parent.parent)


class Settings(BaseSettings):
    app_title = 'FASTAPI_PLOTLY'
    api_prefix = '/api'

    prod_mode: bool = False

    class Config:
        _env_file = os.path.join(BASE_DIR, '.env')
        if os.path.exists(_env_file):
            env_file = _env_file



settings = Settings()
