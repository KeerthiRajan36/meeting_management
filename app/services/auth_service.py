from sqlalchemy.orm import Session

from fastapi import HTTPException

from app.models.user import User

from app.schemas.auth import (
    RegisterSchema,
    LoginSchema
)

from app.utils.password import (
    hash_password,
    verify_password
)

from app.utils.jwt import (
    create_access_token
)



def register_user(
        db:Session,
        data:RegisterSchema
):

    existing=db.query(User).filter(
        User.username==data.username
    ).first()


    if existing:

        raise HTTPException(
            400,
            "Username already exists"
        )


    user=User(

        username=data.username,

        password=hash_password(
            data.password
        ),

        role=data.role
    )


    db.add(user)

    db.commit()

    db.refresh(user)


    return user





def login_user(
        db:Session,
        data:LoginSchema
):


    user=db.query(User).filter(
        User.username==data.username
    ).first()



    if not user:

        raise HTTPException(
            401,
            "Invalid username/password"
        )



    if not verify_password(
        data.password,
        user.password
    ):

        raise HTTPException(
            401,
            "Invalid username/password"
        )



    token=create_access_token(

        {
            "sub":user.username,

            "role":user.role
        }

    )


    return {

        "access_token":token,

        "token_type":"bearer"

    }