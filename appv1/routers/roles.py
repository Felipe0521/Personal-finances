from typing import List
from fastapi import APIRouter, Depends, HTTPException
from appv1.crud.rol import create_rol_sql, get_all_roles
from appv1.crud.users import create_user_sql, get_user_by_email
from appv1.schemas.rol import RolCreate, RolResponse

from core.security import get_hashed_password
from db.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
router = APIRouter()


@router.post("/rol/create")
async def insert_role(rol: RolCreate, db: Session = Depends(get_db)):
    respuesta = create_rol_sql(db, rol)
    if respuesta:
      return {"mensaje":"rol creado con exito"}


@router.get("/rol/get_all/", response_model=List[RolResponse])
async def read_all_roles(db:Session = Depends(get_db) ):
   roles = get_all_roles(db)
   if len(roles) == 0:
       raise HTTPException(status_code=500, detail="No hay roles")
   return roles