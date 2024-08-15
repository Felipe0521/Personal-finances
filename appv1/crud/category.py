from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from appv1.schemas.category import CategoryCreate, CategoryResponse

from sqlalchemy.exc import SQLAlchemyError, IntegrityError


def create_category_sql(db: Session, category: CategoryCreate):

    try:
        sql_query = text(
            "INSERT INTO category (category_name, category_description) "
            "VALUES (:category_name, :category_description)"
        )
        params = {
            "category_name": category.category_name,
            "category_description": category.category_description
        }
        db.execute(sql_query, params)
        db.commit()
        return True  # Retorna True si la inserción fue exitosa
    
    except IntegrityError as e:
            db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
            print(f"Error al crear la categoria: {e}")
            if 'Duplicate entry' in str(e.orig):
             if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El ID del categoria ya está en uso")
            else:
             raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear la categoria")
    
    except SQLAlchemyError as e:
            db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
            print(f"Error al crear la categoria: {e}")
            raise HTTPException(status_code=500, detail="Error al crear la categoria")
   

def get_category_by_name(db: Session, name: str):
    try:
         sql = text("SELECT * FROM category WHERE category_name = :name")
         result = db.execute(sql, {"name": name}).fetchone()
         return result
    except SQLAlchemyError as e:
            db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
            print(f"Error al obtener la categoria: {e}")
            raise HTTPException(status_code=500, detail="Error al obtener la categoria")
    

def get_all_categories(db: Session):
    try:
         sql = text("SELECT * FROM category")
         result = db.execute(sql).fetchall()
         return result
    except SQLAlchemyError as e:
            db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
            print(f"Error al obtener categorias: {e}")
            raise HTTPException(status_code=500, detail="Error al buscar las categorias")

