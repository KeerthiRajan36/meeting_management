from sqlalchemy import Column,Integer,String,Boolean
from app.database.database import Base



class Room(Base):

    __tablename__="rooms"


    id = Column(
        Integer,
        primary_key=True
    )


    room_name = Column(
        String,
        unique=True
    )


    capacity = Column(
        Integer
    )


    location = Column(
        String
    )


    is_available = Column(
        Boolean,
        default=True
    )