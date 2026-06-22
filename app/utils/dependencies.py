from fastapi import Depends,HTTPException

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from sqlalchemy.orm import Session

from jose import jwt,JWTError


from app.database.database import get_db


from app.models.user import User


from app.utils.jwt import (

    SECRET_KEY,

    ALGORITHM

)




security=HTTPBearer()





def get_current_user(

    credential:HTTPAuthorizationCredentials=Depends(security),

    db:Session=Depends(get_db)

):

    token=credential.credentials
    try:


        payload=jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[ALGORITHM]

        )



        username=payload.get(
            "sub"
        )



    except JWTError:


        raise HTTPException(

            status_code=401,

            detail="Invalid token"

        )





    user=db.query(User).filter(

        User.username==username

    ).first()



    if not user:


        raise HTTPException(

            status_code=404,

            detail="User not found"

        )



    return user





def admin_required(

    user=Depends(get_current_user)

):


    if user.role!="Admin":


        raise HTTPException(

            status_code=403,

            detail="Admin access required"

        )


    return user