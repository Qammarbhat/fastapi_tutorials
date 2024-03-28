from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from helpers import BlogModel
from schemas import UserBase, UserDisplay, DoctorBase, DoctorDisplay, PatientBase
from db.database import get_db
from db import db_user


router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# Create User
@router.post("/add_user", summary="Create a new user", response_model= UserDisplay)
def create_user(request: UserBase, db: Session= Depends(get_db)):
    return db_user.create_user(db, request)

 
@router.post("/add_doctor", summary="Add doctor to Data Base", response_model= DoctorDisplay)
def create_doctor(request: DoctorBase, db: Session=Depends(get_db)):
    return db_user.create_doctor(db, request)

@router.post("/add_patient", summary="Patient Appointment Booking")
def create_patient(request: PatientBase, db: Session=Depends(get_db)):
    return db_user.create_patient(db, request)



# Read All Users
@router.get("/get_all_users", summary="Read All Users", response_model= List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

# Read One user using id
@router.get("/get_one_user/{id}", summary="Read one user", response_model=UserDisplay)
def get_one_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_one_user(db, id)

# Update User
@router.post("/update_user/{id}", summary= "Updates a user deets")
def update_user(id: int, request: UserBase, db: Session= Depends(get_db)):
    return db_user.update_user(db, id, request)

# Delete User
@router.get("/delete_user/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)