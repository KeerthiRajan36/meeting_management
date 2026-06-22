from pydantic import BaseModel



class RoomCreate(BaseModel):

    room_name:str

    capacity:int

    location:str

    is_available:bool=True



class RoomUpdate(BaseModel):

    room_name:str|None=None

    capacity:int|None=None

    location:str|None=None

    is_available:bool|None=None



class RoomResponse(BaseModel):

    id:int

    room_name:str

    capacity:int

    location:str

    is_available:bool



    class Config:

        from_attributes=True