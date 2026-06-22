from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session


from app.database.database import get_db


from app.schemas.room import (
    RoomCreate,
    RoomUpdate,
    RoomResponse
)


from app.services import room_service


from app.utils.dependencies import admin_required



router=APIRouter(

    prefix="/rooms",

    tags=["Rooms"]

)




@router.post(
    "",
    response_model=RoomResponse,
    dependencies=[
        Depends(admin_required)
    ]
)
def create_room(

    data:RoomCreate,

    db:Session=Depends(get_db)

):

    return room_service.create_room(

        db,

        data

    )





@router.get(
    "",
    response_model=list[RoomResponse]
)
def get_rooms(

    capacity:int|None=None,

    db:Session=Depends(get_db)

):

    return room_service.get_rooms(

        db,

        capacity

    )





@router.get(
    "/{id}",
    response_model=RoomResponse
)
def get_room(

    id:int,

    db:Session=Depends(get_db)

):

    return room_service.get_room(

        db,

        id

    )





@router.put(
    "/{id}",
    response_model=RoomResponse,
    dependencies=[
        Depends(admin_required)
    ]
)
def update_room(

    id:int,

    data:RoomUpdate,

    db:Session=Depends(get_db)

):

    return room_service.update_room(

        db,

        id,

        data

    )