from pydantic import BaseModel

class Task(BaseModel):
    tasknumber: int
    details: str
    due_by: str
    status:str
