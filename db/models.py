from sqlalchemy.sql.sqltypes import String, Boolean, Integer
from sqlalchemy.sql.schema import Column, ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship




class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index= True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    items = relationship("DbArticle", back_populates="user")

class DbDoctors(Base):
    __tablename__="doctors"
    id= Column(Integer, primary_key=True, index=True)
    username= Column(String)
    clinic_address = Column(String)
    speciality= Column(String)
    public_id= Column(String)
    appointments = relationship("DbPatients", back_populates= "appointment_with")

class DbPatients(Base):
    __tablename__ ="patients"
    id = Column(Integer, primary_key=True, index= True)
    patient_name = Column(String)
    patient_age = Column(Integer)
    patient_appointment_date = Column(String)

    doctor_public_id= Column(Integer, ForeignKey("doctors.public_id")) 
    appointment_with= relationship("DbDoctors", back_populates="appointments")

class DbArticle(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content= Column(String)
    published= Column(Boolean)
    
    user_id= Column(Integer, ForeignKey("users.id"))
    user = relationship("DbUser", back_populates="items")
