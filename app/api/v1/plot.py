from fastapi import APIRouter
from app.graphics.plot import get_plot_html
from fastapi.responses import HTMLResponse

plot_router = APIRouter()

@plot_router.get("", response_class=HTMLResponse)
def get_plot(from_x: float, to_x: float, step: float):
    return get_plot_html(from_x, to_x, step)

