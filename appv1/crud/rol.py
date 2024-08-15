from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text

from appv1.schemas.rol import RolCreate
from core.security import get_hashed_password
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


def create_rol_sql(db: Session, role: RolCreate):

    try:
        sql_query = text(
            "INSERT INTO roles (rol_name) "
            "VALUES (:rol_name)"
        )
        params = {
            "rol_name": role.rol_name
        }
        db.execute(sql_query, params)
        db.commit()
        return True  # Retorna True si la inserción fue exitosa
    
    except IntegrityError as e:
            db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
            print(f"Error al crear el rol: {e}")
            if 'Duplicate entry' in str(e.orig):
             if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El ID del rol ya está en uso")
            else:
             raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear el rol")
    
    except SQLAlchemyError as e:
            db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
            print(f"Error al crear el rol: {e}")
            raise HTTPException(status_code=500, detail="Error al crear el rol")
   

def get_all_roles(db: Session):
    try:
         sql = text("SELECT * FROM roles")
         result = db.execute(sql).fetchall()
         return result
    except SQLAlchemyError as e:
            db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
            print(f"Error al obtener roles: {e}")
            raise HTTPException(status_code=500, detail="Error al buscar roles")


