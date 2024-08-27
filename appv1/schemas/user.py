from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated, List, Optional
from datetime import datetime


class UserBase(BaseModel):
    user_id: str
    full_name: Annotated[str, StringConstraints(max_length=80)]
    mail: EmailStr
    user_role: Annotated[str, StringConstraints(max_length=15)]
    

class UserCreate(BaseModel):
    full_name: str
    mail: str
    user_role: str
    passhash: str
    
class UserResponse(BaseModel):
    user_id: str
    full_name: str
    mail: str
    user_role: str
    user_status: bool = True
    created_at: datetime
    updated_at: datetime

class UserUpdate(BaseModel):
    full_name: Optional[Annotated[str, StringConstraints(max_length=80)]] = None
    mail: Optional[EmailStr] = None
    user_role: Optional[Annotated[str, StringConstraints(max_length=15)]] = None
    user_status: bool = None

class PaginatedUsersResponse(BaseModel):
    users: List[UserResponse]
    total_pages: int
    current_page: int
    page_size: int

class UserLoggin(UserBase):
    user_id: str

class ResponseLoggin(BaseModel):
    user: UserLoggin
    access_token: str