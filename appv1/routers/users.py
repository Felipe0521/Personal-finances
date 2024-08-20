from typing import List
from fastapi import APIRouter, Depends, HTTPException
from appv1.crud.users import create_user_sql, delete_user, get_all_users, get_all_users_paginated, get_user_by_email, get_user_by_id, get_user_by_role, update_user
from appv1.schemas.user import PaginatedUsersResponse, UserCreate, UserResponse, UserUpdate
from db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/user/create")
async def insert_user(user: UserCreate, db: Session = Depends(get_db)):
    respuesta = create_user_sql(db, user)
    if respuesta:
      return {"mensaje":"usuario registrado con exito"}


@router.get("/user/get_user_email/", response_model=UserResponse)
async def read_user_by_email(email:str, db:Session = Depends(get_db) ):
   ususario = get_user_by_email(db, email)
   if ususario is None:
       raise HTTPException(status_code=500, detail="Usuario no encontrado")
   
   return ususario

@router.get("/user/get_all/", response_model=List[UserResponse])
async def read_all_users(db:Session = Depends(get_db) ):
   usuarios = get_all_users(db)
   if len(usuarios) == 0:
       raise HTTPException(status_code=500, detail="No hay usuarios")
   return usuarios

@router.get("/user/get_users_by_rol/", response_model=List[UserResponse])
async def read_users_by_rol( role: str,db:Session = Depends(get_db) ):
   usuarios = get_user_by_role(db, role)
   if len(usuarios) == 0:
       raise HTTPException(status_code=500, detail="No hay usuarios")
   return usuarios

# Endpoint para actualizar un usuario
@router.put("/update/", response_model=dict)
def update_user_by_id(user_id: str, user: UserUpdate, db: Session = Depends(get_db)):
    usero = get_user_by_id(db, user_id)
    if usero is None:
         raise HTTPException(status_code=500, detail="No hay usuario encontrado")
    db_user = update_user(db, user_id, user)
    if db_user:
     return {"mensaje": "registro actualizado con éxito" }
    
# usuarios paginados
@router.get("/users-by-page/", response_model=PaginatedUsersResponse)
def get_all_users_by_page(page: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
    
    users, total_pages = get_all_users_paginated(db, page, page_size)
    return {
        "users": users,
        "total_pages": total_pages,
        "current_page": page,
        "page_size": page_size
          }

@router.delete("/delete/{user_id}", response_model=dict)
def delete_user_by_id(user_id: str, db: Session = Depends(get_db)):
     usero = get_user_by_id(db, user_id)
     if usero is None:
         raise HTTPException(status_code=500, detail="No hay usuario encontrado")

     result = delete_user(db, user_id)
     if result:
        return {"mensaje": "Usuario eliminado con éxito"}
     
