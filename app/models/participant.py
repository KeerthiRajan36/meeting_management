from sqlalchemy import Column,Integer,String,ForeignKey

from app.database.database import Base



class Participant(Base):

    __tablename__="participants"


    id = Column(
        Integer,
        primary_key=True
    )


    booking_id = Column(
        Integer,
        ForeignKey("bookings.id")
    )


    name = Column(
        String
    )


    email = Column(
        String
    )