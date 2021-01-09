from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import markdown
from app.api.api_v1.api import router as api_router

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def main():
    with open('readme.md', 'r') as f:
        content = f.read()
    
        return markdown.markdown(content)


app.include_router(api_router, prefix="/api/v1")
