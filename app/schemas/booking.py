from pydantic import BaseModel,field_validator

from datetime import datetime



class BookingCreate(BaseModel):

    employee_id:int

    room_id:int

    meeting_title:str

    start_time:datetime

    end_time:datetime



    @field_validator(
        "end_time"
    )
    def validate_end_time(
        cls,
        value,
        info
    ):


        start=info.data.get(
            "start_time"
        )


        if start and value <= start:

            raise ValueError(
                "End time must be greater than start time"
            )


        return value





class BookingResponse(BaseModel):

    id:int

    employee_id:int

    room_id:int

    meeting_title:str

    start_time:datetime

    end_time:datetime



    class Config:

        from_attributes=True