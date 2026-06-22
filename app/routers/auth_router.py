from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.database.database import get_db

from app.schemas.auth import (
    RegisterSchema,
    LoginSchema,
    TokenSchema
)

from app.services import auth_service



router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)



@router.post("/register")
def register(

    data:RegisterSchema,

    db:Session=Depends(get_db)

):

    return auth_service.register_user(
        db,
        data
    )





@router.post(
    "/login",
    response_model=TokenSchema
)
def login(

    data:LoginSchema,

    db:Session=Depends(get_db)

):

    return auth_service.login_user(
        db,
        data
    )