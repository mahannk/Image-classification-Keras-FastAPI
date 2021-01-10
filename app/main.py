from fastapi import FastAPI, status, Response
from fastapi.responses import HTMLResponse
import markdown
from app.api.api_v1.api import router as api_router
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def main():
    with open('readme.md', 'r') as f:
        content = f.read()
    
        return markdown.markdown(content)


app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', '5000'))
