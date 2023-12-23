from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Serve static files (React app)
app.mount("/static", StaticFiles(directory="build/static"), name="static")


# Catch-all route for non-API routes
@app.get("/{path:path}", include_in_schema=False)
async def serve_react_app(path: str):
    index_file_path = os.path.join("build", "index.html")
    return FileResponse(index_file_path)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=3000)
