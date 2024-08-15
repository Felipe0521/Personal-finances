from typing import List
from fastapi import APIRouter, Depends, HTTPException
from appv1.crud.category import create_category_sql, get_category_by_name, get_all_categories

from appv1.schemas.category import CategoryCreate, CategoryResponse

from core.security import get_hashed_password
from db.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
router = APIRouter()


@router.post("/category/create")
async def insert_category(category: CategoryCreate, db: Session = Depends(get_db)):
    respuesta = create_category_sql(db, category)
    if respuesta:
      return {"mensaje":"categoria creada con exito"}


@router.get("/category/get_category_by_name/", response_model=CategoryResponse)
async def read_category_by_name(name:str, db:Session = Depends(get_db) ):
   category = get_category_by_name(db, name)
   if category is None:
       raise HTTPException(status_code=500, detail="Categoria no encontrada")
   
   return category


@router.get("/category/get_all/", response_model=List[CategoryResponse])
async def read_all_categories(db:Session = Depends(get_db) ):
   categorias = get_all_categories(db)
   if len(categorias) == 0:
       raise HTTPException(status_code=500, detail="No hay categorias")
   return categorias