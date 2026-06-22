from sqlalchemy.orm import Session

from app.models.participant import Participant

from app.models.booking import Booking

from app.models.room import Room

from app.schemas.participant import (
    ParticipantCreate
)

from app.exceptions.custom_exception import (
    BadRequestException
)



def add_participant(
        db:Session,
        booking_id:int,
        data:ParticipantCreate
):


    booking=db.query(
        Booking
    ).filter(
        Booking.id==booking_id
    ).first()



    room=db.query(
        Room
    ).filter(
        Room.id==booking.room_id
    ).first()



    count=db.query(
        Participant
    ).filter(
        Participant.booking_id==booking_id
    ).count()



    if count >= room.capacity:

        raise BadRequestException(
            "Room capacity exceeded"
        )



    participant=Participant(

        booking_id=booking_id,

        **data.model_dump()

    )


    db.add(participant)

    db.commit()

    db.refresh(participant)


    return participant





def get_participants(
        db,
        booking_id
):


    return db.query(
        Participant
    ).filter(
        Participant.booking_id==booking_id
    ).all()