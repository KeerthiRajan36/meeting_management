from fastapi import Request

from fastapi.responses import JSONResponse


from app.exceptions.custom_exception import (

    NotFoundException,

    BadRequestException,

    UnauthorizedException

)





async def not_found_handler(

        request:Request,

        exc:NotFoundException

):


    return JSONResponse(

        status_code=404,

        content={

            "error":exc.message

        }

    )





async def bad_request_handler(

        request:Request,

        exc:BadRequestException

):


    return JSONResponse(

        status_code=400,

        content={

            "error":exc.message

        }

    )





async def unauthorized_handler(

        request:Request,

        exc:UnauthorizedException

):


    return JSONResponse(

        status_code=401,

        content={

            "error":exc.message

        }

    )