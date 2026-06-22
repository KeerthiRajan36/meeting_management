from sqlalchemy.orm import Session

from app.models.employee import Employee

from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate
)

from app.exceptions.custom_exception import (
    NotFoundException
)



def create_employee(
        db:Session,
        data:EmployeeCreate
):


    employee=Employee(
        **data.model_dump()
    )


    db.add(employee)

    db.commit()

    db.refresh(employee)


    return employee





def get_all_employees(
        db:Session,
        department=None
):

    query=db.query(Employee)


    if department:

        query=query.filter(
            Employee.department==department
        )


    return query.all()





def get_employee(
        db:Session,
        employee_id:int
):


    employee=db.query(Employee).filter(
        Employee.id==employee_id
    ).first()



    if not employee:

        raise NotFoundException(
            "Employee not found"
        )


    return employee





def update_employee(
        db:Session,
        employee_id:int,
        data:EmployeeUpdate
):


    employee=get_employee(
        db,
        employee_id
    )



    for key,value in data.model_dump(
        exclude_unset=True
    ).items():

        setattr(
            employee,
            key,
            value
        )


    db.commit()

    db.refresh(employee)


    return employee