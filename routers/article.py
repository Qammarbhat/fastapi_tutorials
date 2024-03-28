from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from helpers import BlogModel
from schemas import UserBase, UserDisplay, DoctorBase, DoctorDisplay, PatientBase, ArticleBase, ArticleDisplay
from db.database import get_db
from db import db_article


router = APIRouter(
    prefix="/article",
    tags=["article"]
)

# create article
@router.post("/create", response_model= ArticleDisplay)
def create_article(request: ArticleBase, db: Session= Depends(get_db)):
    return db_article.create_article(db, request)


@router.get("/get-article/{id}", response_model= ArticleDisplay)
def get_article(id: int, db: Session= Depends(get_db)):
    return db_article.get_article(db, id)