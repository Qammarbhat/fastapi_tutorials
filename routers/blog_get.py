from fastapi import APIRouter, status, Response, Depends
from helpers import BlogType, required_functionality
from typing import Optional



router = APIRouter(
    prefix="/blog",
    tags=["blog"]
    
)

# Retrieve all blogs endpoint with optional pagination parameters.
@router.get("/all",
         
         summary="Retrieve all blogs",
         description='This API endpoint simulates fetching all blogs.',
         response_description="The list of available blogs"
         )
def get_all_blogs(page: int = 1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionality)):
    """
    Retrieve all blogs with optional pagination parameters.
    - **page**: mandatory query parameter, default is 1.
    - **page_size**: optional query parameter, represents the number of blogs per page.
    """
    return {"message": f"All {page_size} blogs on page {page}", "req": req_parameter}

# Retrieve a comment of a blog by providing blog ID and comment ID.
@router.get("/{id}/comments/{comment_id}",
        tags=["comment"],
        summary="Retrieve a comment of a blog",
        )
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog.
    - **id**: mandatory path parameter representing the blog ID.
    - **comment_id**: mandatory path parameter representing the comment ID.
    - **valid**: optional query parameter indicating if the comment is valid.
    - **username**: optional query parameter representing the username.
    """
    return {"message": f"Blog_id: {id}, Comment_ID: {comment_id}, valid: {valid}, username: {username}"}

# Retrieve blogs of a specific type using a custom enum class.
@router.get("/type/{type}",
         summary="Retrieve blogs of a specific type",
         )
def get_blog_type(type: BlogType):
    """
    Retrieve blogs of a specific type.
    - **type**: mandatory path parameter representing the blog type.
    """
    return {"message": f"Blog type is: {type}"}

# Retrieve a blog by ID, handling different HTTP status codes.
@router.get('/{id}',
         status_code=status.HTTP_200_OK,
         summary="Retrieve a blog by ID"
         )
def get_blog(id: int, response: Response):
    """
    Retrieve a blog by ID.
    - **id**: mandatory path parameter representing the blog ID.
    - **response**: FastAPI Response object to handle status code.
    """
    
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"Blog {id} not found"}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"Blog with id: {id}"}
