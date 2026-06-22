from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session


from app.database.database import get_db


from app.schemas.participant import (
    ParticipantCreate,
    ParticipantResponse
)


from app.services import participant_service



router=APIRouter(

    prefix="/bookings",

    tags=["Participants"]

)





@router.post(
    "/{booking_id}/participants",
    response_model=ParticipantResponse
)
def add_participant(

    booking_id:int,

    data:ParticipantCreate,

    db:Session=Depends(get_db)

):


    return participant_service.add_participant(

        db,

        booking_id,

        data

    )





@router.get(
    "/{booking_id}/participants",
    response_model=list[ParticipantResponse]
)
def get_participants(

    booking_id:int,

    db:Session=Depends(get_db)

):


    return participant_service.get_participants(

        db,

        booking_id

    )