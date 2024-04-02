from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/", response_class=FileResponse)
def get_template():
    return FileResponse("templates/index.html")
