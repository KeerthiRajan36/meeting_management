from sqlalchemy.orm import Session

from app.models.room import Room

from app.schemas.room import (
    RoomCreate,
    RoomUpdate
)


from app.exceptions.custom_exception import (
    NotFoundException
)



def create_room(
        db:Session,
        data:RoomCreate
):


    room=Room(
        **data.model_dump()
    )


    db.add(room)

    db.commit()

    db.refresh(room)


    return room





def get_rooms(
        db:Session,
        capacity=None
):


    query=db.query(Room)



    if capacity:

        query=query.filter(
            Room.capacity>=capacity
        )


    return query.all()





def get_room(
        db:Session,
        room_id:int
):


    room=db.query(Room).filter(
        Room.id==room_id
    ).first()



    if not room:

        raise NotFoundException(
            "Room not found"
        )


    return room





def update_room(
        db:Session,
        room_id:int,
        data:RoomUpdate
):


    room=get_room(
        db,
        room_id
    )



    for key,value in data.model_dump(
        exclude_unset=True
    ).items():

        setattr(
            room,
            key,
            value
        )


    db.commit()

    db.refresh(room)


    return room