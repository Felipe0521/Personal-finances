from pydantic import BaseModel
from datetime import datetime

class CategoryCreate(BaseModel):
    category_name: str
    category_description: str
    
   
class CategoryResponse(BaseModel):
    category_id: int
    category_name: str
    category_description: str
    category_status: int = 1
    