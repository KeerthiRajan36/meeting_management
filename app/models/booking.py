from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from app.database.database import Base



class Booking(Base):

    __tablename__="bookings"


    id = Column(
        Integer,
        primary_key=True
    )


    employee_id = Column(
        Integer,
        ForeignKey("employees.id")
    )


    room_id = Column(
        Integer,
        ForeignKey("rooms.id")
    )


    meeting_title = Column(
        String
    )


    start_time = Column(
        DateTime
    )


    end_time = Column(
        DateTime
    )

    participants=relationship(
        "Participant",
        cascade="all,delete"
    )