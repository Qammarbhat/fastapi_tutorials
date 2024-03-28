from pydantic import BaseModel

class PatientBase(BaseModel):
    patient_name: str
    patient_age: int
    patient_appointment_date: str
    appointment_with: str

class DoctorBase(BaseModel):
    username: str
    clinic_address : str
    speciality: str
    

class DoctorDisplay(BaseModel):
    username: str
    public_id: str
    class config():
        orm_mode = True

# Article which goes inside UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool
    class config():
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    items: list[Article] = []
    class config():
        orm_mode = True

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int

# User that goes inside ArticleDisplay
class User(BaseModel):
    id: int
    username: str
    class config():
        orm_mode = True

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    class config():
        orm_mode = True