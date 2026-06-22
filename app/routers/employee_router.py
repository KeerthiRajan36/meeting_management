from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.database.database import get_db


from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse
)


from app.services import employee_service


from app.utils.dependencies import admin_required



router=APIRouter(

    prefix="/employees",

    tags=["Employees"]

)




@router.post(
    "",
    response_model=EmployeeResponse,
    dependencies=[
        Depends(admin_required)
    ]
)
def create_employee(

    data:EmployeeCreate,

    db:Session=Depends(get_db)

):

    return employee_service.create_employee(

        db,

        data

    )





@router.get(
    "",
    response_model=list[EmployeeResponse]
)
def get_employees(

    department:str|None=None,

    db:Session=Depends(get_db)

):

    return employee_service.get_all_employees(

        db,

        department

    )





@router.get(
    "/{id}",
    response_model=EmployeeResponse
)
def get_employee(

    id:int,

    db:Session=Depends(get_db)

):

    return employee_service.get_employee(

        db,

        id

    )





@router.put(
    "/{id}",
    response_model=EmployeeResponse,
    dependencies=[
        Depends(admin_required)
    ]
)
def update_employee(

    id:int,

    data:EmployeeUpdate,

    db:Session=Depends(get_db)

):

    return employee_service.update_employee(

        db,

        id,

        data

    )