from fastapi import APIRouter
from app.api.v1.plot import plot_router


api_v1_router = APIRouter(prefix='/v1')
api_v1_router.include_router(plot_router, prefix='/plot', tags=['Plot'])