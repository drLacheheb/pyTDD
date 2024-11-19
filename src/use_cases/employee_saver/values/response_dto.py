from pydantic import BaseModel


class ResponseDTO(BaseModel):
    executed: bool
    exception_occurred: bool
