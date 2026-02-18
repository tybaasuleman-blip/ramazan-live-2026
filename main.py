import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# 1. Initialize FastAPI
app = FastAPI()

# 2. Mount Static Folder (Critical for your audio.mp3)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 3. Setup Jinja2 Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Renders the Ramazan Dashboard. 
    Data can be passed to the HTML via the context dictionary.
    """
    context = {
        "request": request,
        "title": "Ramazan Mubarak 2026 | LIVE",
        "message": "May this Ramazan be the bestest in your life.",
        "dua": "May all your dreams—and mine—come true this year. ⚡"
    }
    return templates.TemplateResponse("index.html", context)

# Local running logic (Production servers will ignore this and use Uvicorn directly)
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)