from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()


@app.get("/")
def root(request: Request):
    return {"monorepo": "deployed!"}
