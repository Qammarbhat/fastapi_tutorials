from db.database import SessionLocal
from schemas import UserBase, DoctorBase, PatientBase
from db.models import DbUser, DbDoctors, DbPatients
from fastapi import HTTPException, status
from db.hash import Hash
from sqlalchemy.orm.session import Session
import random
import string


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username= request.username,
        email= request.email,
        password= Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def create_doctor(db: Session, request: DoctorBase):
    new_doctor = DbDoctors(
        username= request.username,
        clinic_address = request.clinic_address,
        speciality= request.speciality,
        public_id= ''.join(random.choices(string.ascii_letters + string.digits, k=4))

    )

    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return new_doctor

def create_patient(db: Session, request: PatientBase):
    new_patient = DbPatients(
        patient_name= request.patient_name,
        patient_age= request.patient_age,
        patient_appointment_date = request.patient_appointment_date
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

def get_all_users(db: Session):
    return db.query(DbUser).all()

def get_one_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} not found")
    return user


def update_user(db: Session, id: int, request: UserBase):
    user= db.query(DbUser).filter(DbUser.id == id)
    if not user.first:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} not found")
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
        })
    db.commit()
    return "UPDATED"


def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"user with id {id} not found")
    db.delete(user)
    db.commit()
    return "Deleted"