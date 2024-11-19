from pydantic import BaseModel


class EmployeeDTO(BaseModel):
    first_name: str
    last_name: str
