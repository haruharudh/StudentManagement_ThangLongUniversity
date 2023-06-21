from fastapi import Depends, FastAPI, Request, Form,status,Header,APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy import exists
from sqlalchemy.orm import Session
from model import BillSchema,StudentSchema,CourseSchema,ClassSchema
from database import SessionLocal, engine
import model

router = APIRouter()  
model.Base.metadata.create_all(bind=engine)


def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.post("/create_bill")
async def create_bill(
    db: Session = Depends(get_database_session),
    studentID: str = Form(...),
    termID: str = Form(...),
    subjectID: str = Form(...),
    status: int = Form(...)
):
    student_exists = db.query(exists().where(ClassSchema.studentID == studentID)).scalar()
    term_exists = db.query(exists().where(CourseSchema.))