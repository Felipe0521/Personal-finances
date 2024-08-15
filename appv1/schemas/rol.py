from pydantic import BaseModel
from datetime import datetime

class RolCreate(BaseModel):
    rol_name: str
   
class RolResponse(BaseModel):
    rol_name: str
   