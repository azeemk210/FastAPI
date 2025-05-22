from .. import models, schemas, utils	
from fastapi import FastAPI, status, HTTPException, Depends, Response, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Hash the password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password


    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user