from fastapi import FastAPI

from app.database.database import engine,Base

from app.routers import (

    auth_router,

    employee_router,

    room_router,

    booking_router,

    participant_router

)

from app.exceptions.custom_exception import (

    NotFoundException,

    BadRequestException,

    UnauthorizedException

)


from app.exceptions.handler import (

    not_found_handler,

    bad_request_handler,

    unauthorized_handler

)

import app.models


Base.metadata.create_all(
    bind=engine
)



app=FastAPI(

    title="Meeting Room Booking System",

    version="1.0"

)



# Exception Registration

app.add_exception_handler(

    NotFoundException,

    not_found_handler

)


app.add_exception_handler(

    BadRequestException,

    bad_request_handler

)


app.add_exception_handler(

    UnauthorizedException,

    unauthorized_handler

)



# Routers

app.include_router(
    auth_router.router
)


app.include_router(
    employee_router.router
)


app.include_router(
    room_router.router
)


app.include_router(
    booking_router.router
)


app.include_router(
    participant_router.router
)



@app.get("/")
def home():

    return {

        "message":
        "Meeting Room Booking API Running"

    }