from colour import Color
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image as im
from pydantic import BaseModel
from tqdm import tqdm
import numpy as np
import io


from . import settings

from my_library.my_module.my_functions import mandelbrot, mandelbrot_image


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    """
    Splashpage.
    """

    centre = complex(0.0, 0.0)
    zoom = 0.5

    return settings.templates.TemplateResponse(
        "pages/index.html", {"request": request, "centre": centre, "zoom": zoom}
    )


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


@app.get("/mandelbrot_image/{real}/{imag}/{zoom}/{res}")
async def sample_mandelbrot_area(real: float, imag: float, zoom: float, res: int):
    """
    Evaluate an area of complex numbers.
    """

    center = complex(real, imag)
    resolution = (res, res)
    levels = 80

    red = Color("red")
    blue = Color("blue")
    cmap = list(red.range_to(blue, levels + 1))

    data = mandelbrot_image(center, 1.0 / zoom, resolution, levels)
    shape = data.shape

    colours = np.zeros((shape[1], shape[0], 3), dtype=np.uint8)

    for n in tqdm(range(resolution[0] * resolution[1])):
        j = n % resolution[1]
        i = n // resolution[1]
        [r, g, b] = cmap[int(data[i, j])].rgb
        colours[j, i, 0] = r * 255.0
        colours[j, i, 1] = g * 255.0
        colours[j, i, 2] = b * 255.0

    image = im.fromarray(colours)
    imgio = io.BytesIO()
    image.save(imgio, "JPEG")
    imgio.seek(0)

    return StreamingResponse(content=imgio, media_type="image/jpeg")
