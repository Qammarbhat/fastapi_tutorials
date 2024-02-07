from typing import Optional, List
from fastapi import APIRouter, Query, Path, Body, Path
from helpers import BlogModel


router = APIRouter(
    prefix="/blog",
    tags=["bog"]
)

@router.post("/new")
def create_blog(blog: BlogModel):
    return {"data": blog} 

@router.post("/new/{id}")
async def create_blog(blog: BlogModel, id: int, version: int =1):
    return {"data": f"Blog: {blog}, id: {id}, version: {version}"} 

@router.post("/new/{id}/comment/{comment_id}")
async def create_comment(blog: BlogModel, id: int, 
                         comment_title: str = Query(None, 
                                                 title="Title of the comment", 
                                                 description="The description of the comment title", alias="commentTitle", 
                                                 deprecated= True),
                        patient_id: int = Query(None, description="ID of the patient", alias="patientID"),
                        
                        content: str= Body(...,
                                           min_length=10,
                                           max_length=100,
                                           regex="^[a-z\s]*$"),
                        v: Optional[List[str]]= Query(["hello1", "hello2", "hello3"]),

                        comment_id: int =Path(gt=5, le=10)
                        ):
                        
    return{
        "body": blog,
        "id": id,
        "comment_title": comment_title,
        "patient_id": patient_id,
        "content": content,
        "version": v,
        "comment_id": comment_id
    }