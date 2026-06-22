from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.database.database import get_db


from app.schemas.booking import (
    BookingCreate,
    BookingResponse
)


from app.services import booking_service


from app.utils.dependencies import (
    get_current_user
)



router=APIRouter(

    prefix="/bookings",

    tags=["Bookings"]

)





@router.post(
    "",
    response_model=BookingResponse
)
def create_booking(

    data:BookingCreate,

    db:Session=Depends(get_db),

    user=Depends(get_current_user)

):


    return booking_service.create_booking(

        db,

        data

    )





@router.get(
    "",
    response_model=list[BookingResponse]
)
def get_bookings(

    date:str|None=None,

    page:int=1,

    limit:int=10,

    db:Session=Depends(get_db)

):


    return booking_service.get_bookings(

        db,

        date,

        page,

        limit

    )





@router.get(
    "/{id}",
    response_model=BookingResponse
)
def get_booking(

    id:int,

    db:Session=Depends(get_db)

):


    return booking_service.get_booking(

        db,

        id

    )





@router.delete("/{id}")
def delete_booking(

    id:int,

    db:Session=Depends(get_db),

    user=Depends(get_current_user)

):


    return booking_service.delete_booking(

        db,

        id

    )