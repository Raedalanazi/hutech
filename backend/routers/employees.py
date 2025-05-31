from fastapi import APIRouter, HTTPException
from backend.models.employee import Employee

router = APIRouter()
employees = []

@router.get("/employees")
def get_employees():
    return employees

@router.post("/employees")
def add_employee(employee: Employee):
    employees.append(employee)
    return {"message": "Employee added", "employee": employee}

@router.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for emp in employees:
        if emp.id == employee_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")
