# main.py

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.fetcher import fetch_article_text
from app.summarizer import summarize_text

app = FastAPI()  # ← FastAPI インスタンスが必要！

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def form_post(request: Request, url: str = Form(...)):
    article = fetch_article_text(url)
    summary = summarize_text(article)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "summary": summary
    })
