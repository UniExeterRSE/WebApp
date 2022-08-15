from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
async def homepage():
    """
    Splashpage.
    """

    return "Hello, World!"
