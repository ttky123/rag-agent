from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from routes.query_route import router as query_router
from starlette.middleware.sessions import SessionMiddleware
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
import secrets
import os
app = FastAPI(debug = True)
templates = Jinja2Templates(directory="templates")
# `secrets` 모듈로 키 생성
secret_key = secrets.token_urlsafe(32)


# 세션 미들웨어 추가
if os.getenv("ENV") != "test":
    app.add_middleware(SessionMiddleware, secret_key=secret_key)

app.include_router(query_router)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})