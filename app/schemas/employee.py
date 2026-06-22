from pydantic import BaseModel, EmailStr



class EmployeeCreate(BaseModel):

    name:str

    email:EmailStr

    department:str

    role:str="Employee"



class EmployeeUpdate(BaseModel):

    name:str|None=None

    email:EmailStr|None=None

    department:str|None=None

    role:str|None=None



class EmployeeResponse(BaseModel):

    id:int

    name:str

    email:str

    department:str

    role:str



    class Config:

        from_attributes=True