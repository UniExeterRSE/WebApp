from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from . import settings

from my_library.my_module.my_functions import mandelbrot


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    """
    Splashpage.
    """

    return settings.templates.TemplateResponse("pages/index.html", {"request": request})


class MandelbrotInput(BaseModel):
    real: float
    imag: float
    max_iter: int = 80


@app.get("/mandelbrot")
async def sample_mandelbrot(input: MandelbrotInput):
    """
    Evaluate a single complex number.
    """

    return mandelbrot(complex(input.real, input.imag), input.max_iter)
