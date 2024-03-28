from fastapi import FastAPI
from routers import blog_get, blog_post, article
from routers import user
from db import models
from db.database import engine

app = FastAPI()
app.include_router(article.router)
app.include_router(user.router)
app.include_router(blog_get.router) 
app.include_router(blog_post.router)

# Root endpoint, returns a simple message.
@app.get('/')
def index():
    """
    Root endpoint, returns a simple message.
    """
    return {"message": "Hello World"}

models.Base.metadata.create_all(engine)
