from fastapi import APIRouter

router = APIRouter(
    prefix="/blog",
    tags=["bog"]
)

@router.post("/new")
def create_blog():
    pass