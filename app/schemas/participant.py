from pydantic import BaseModel,EmailStr



class ParticipantCreate(BaseModel):

    name:str

    email:EmailStr



class ParticipantResponse(BaseModel):

    id:int

    booking_id:int

    name:str

    email:str



    class Config:

        from_attributes=True