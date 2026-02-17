from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import SessionLocal
from models.user_model import User
from schemas.user_schema import UserCreate
from core.auth import hash_password, verify_password, create_access_token
from core.index import ApiResponse

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=hash_password(user.password),
        role=user.role
    )
    db.add(db_user)
    db.commit()
    return ApiResponse.success(
        data=db_user,
        message="User created"
    )


@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401)

    token = create_access_token({"sub": user.id})
    return ApiResponse.success(
        data={"access_token": token, "token_type": "bearer"},
    )
