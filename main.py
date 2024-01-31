from fastapi import FastAPI
from routers import blog_get, blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)

# Root endpoint, returns a simple message.
@app.get('/')
def index():
    """
    Root endpoint, returns a simple message.
    """
    return {"message": "Hello World"}

