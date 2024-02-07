### Request Body

#### What?
- **Definition**: The request body is the part of the HTTP request where data is sent by the client to the server.
- **Usage**: It is used to send data to the server, typically for operations like creating or updating a resource.
- **Why?**: Request bodies allow clients to transmit complex data structures to the server, enabling rich interactions and operations.

#### Example:
```python
@router.post("/new")
def create_blog(blog: BlogModel):
    return {"data": blog}
```


### Path and Query Parameters

#### What?
- **Definition**: Path and query parameters are used to pass data within the URL of an HTTP request.
- **Usage**: They allow clients to specify inputs for the server, such as resource identifiers or filtering criteria.
- **Why?**: Path and query parameters make endpoints more dynamic and flexible, enabling customization of requests without altering the endpoint structure.

#### Example:
```python
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
```
### Parameter Metadata

#### What?
- **Definition**: Parameter metadata provides additional information about parameters, such as title, description, alias, or deprecation status.
- **Usage**: It enhances the documentation and understanding of API endpoints, improving usability and developer experience.
- **Why?**: Parameter metadata enables clearer communication between API providers and consumers, aiding in the correct usage of API endpoints.

#### Example:
```python
comment_title: str = Query(None, 
                            title="Title of the comment", 
                            description="The description of the comment title", alias="commentTitle", 
                            deprecated= True),

```
### Validators

#### What?
- **Definition**: Validators are used to enforce constraints or conditions on request parameters or body fields.
- **Usage**: They ensure that data sent to the server meets specified criteria, such as data type, length, format, or range.
- **Why?**: Validators help maintain data integrity, prevent erroneous inputs, and enhance the reliability and security of the API.

#### Example:
```python
content: str= Body(...,
                   min_length=10,
                   max_length=100,
                   regex="^[a-z\s]*$"),
```
### Multiple Values

#### What?
- **Definition**: Multiple values refer to scenarios where an endpoint accepts multiple instances of a parameter or field.
- **Usage**: They enable bulk operations or the handling of multiple entities in a single request.
- **Why?**: Supporting multiple values enhances efficiency, reduces network overhead, and simplifies client-server interactions.

#### Example:
```python
v: Optional[List[str]]= Query(["hello1", "hello2", "hello3"]),
```
### Number Validators

#### What?
- **Definition**: Number validators are validators specifically designed for numerical data types.
- **Usage**: They enforce constraints such as minimum, maximum, greater than, or less than conditions on numeric inputs.
- **Why?**: Number validators ensure data consistency and validity, preventing out-of-range values and potential errors.

#### Example:
```python
comment_id: int =Path(gt=5, le=10)
```
### Complex Subtypes

#### What?
- **Definition**: Complex subtypes are custom data structures or models used within request bodies or parameters.
- **Usage**: They represent more intricate data compositions, allowing for hierarchical or nested structures.
- **Why?**: Complex subtypes facilitate the transmission of sophisticated data, supporting complex business logic and domain requirements.

#### Example:
```python
class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    nb_comments: int
    head: str
    tags: List[str]
    metadata: Dict[str, str] = {"key1": "va1"}
    image: Optional[Image] = None
