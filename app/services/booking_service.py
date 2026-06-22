from sqlalchemy.orm import Session

from app.models.booking import Booking

from app.schemas.booking import BookingCreate

from app.exceptions.custom_exception import (
    BadRequestException,
    NotFoundException
)



def check_room_booking(
        db,
        room_id,
        start,
        end
):


    booking=db.query(
        Booking
    ).filter(

        Booking.room_id==room_id,

        Booking.start_time < end,

        Booking.end_time > start

    ).first()



    if booking:

        raise BadRequestException(
            "Room already booked"
        )





def check_employee_booking(
        db,
        employee_id,
        start,
        end
):


    booking=db.query(
        Booking
    ).filter(

        Booking.employee_id==employee_id,

        Booking.start_time < end,

        Booking.end_time > start

    ).first()



    if booking:

        raise BadRequestException(
            "Employee has another meeting"
        )





def create_booking(
        db:Session,
        data:BookingCreate
):


    check_room_booking(

        db,

        data.room_id,

        data.start_time,

        data.end_time

    )


    check_employee_booking(

        db,

        data.employee_id,

        data.start_time,

        data.end_time

    )



    booking=Booking(
        **data.model_dump()
    )



    db.add(booking)

    db.commit()

    db.refresh(booking)


    return booking





def get_bookings(
        db:Session,
        date=None,
        page=1,
        limit=10
):


    query=db.query(Booking)



    if date:

        query=query.filter(
            Booking.start_time.like(
                f"{date}%"
            )
        )



    offset=(page-1)*limit



    return query.offset(
        offset
    ).limit(
        limit
    ).all()





def get_booking(
        db,
        booking_id
):


    booking=db.query(
        Booking
    ).filter(
        Booking.id==booking_id
    ).first()



    if not booking:

        raise NotFoundException(
            "Booking not found"
        )


    return booking





def delete_booking(
        db,
        booking_id
):


    booking=get_booking(
        db,
        booking_id
    )


    db.delete(booking)

    db.commit()


    return {
        "message":
        "Booking deleted"
    }