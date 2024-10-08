from typing import List, Annotated
from fastapi import APIRouter, Depends, HTTPException
from appv1.crud.permissions import get_all_permissions
from appv1.crud.users import create_user_sql, delete_user, get_all_users, get_all_users_paginated, get_user_by_email, get_user_by_id, get_user_by_role, update_user
from appv1.schemas.user import PaginatedUsersResponse, ResponseLoggin, UserCreate, UserLoggin, UserResponse, UserUpdate

from core.security import get_hashed_password, verify_password, create_access_token, verify_token
from db.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
router = APIRouter()



# @router.get("/login/", response_model=dict)
# async def access(email:str, password: str , db:Session = Depends(get_db) ):
#    ususario = get_user_by_email(db, email)
#    if ususario is None:
#        raise HTTPException(status_code=500, detail="Usuario no encontrado")
   


#    result = verify_password(password, ususario.passhash)
#    if result is None:
#        raise HTTPException(status_code=401, detail="contraseña incorrecta")
#    data = {"sub":ususario.user_id, "rol": ususario.user_role}
#    token = create_access_token(data)
#    return {"token": token}

def authenticate_user(username: str, password: str, db: Session):
    user = get_user_by_email(db, username)
    if not user:
        return False
    if not verify_password(password, user.passhash):
        return False
    return user


@router.post("/token", response_model=ResponseLoggin)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Datos Incorrectos en email o password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": user.user_id, "rol": user.user_role}
    )
    permisos = get_all_permissions(db,user.user_role)
    return ResponseLoggin(
        user=UserLoggin(
            user_id=user.user_id,
            full_name=user.full_name,
            mail=user.mail,
            user_role=user.user_role
        ),
        permissions=permisos,
        access_token=access_token 
    )


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/access/token")

async def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):
    user = await verify_token(token)
    if user is None:
        raise HTTPException(status_code=404, detail="Invalid token")
    user_db = get_user_by_id(db, user)
    if user_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    if not user_db.user_status:
        raise HTTPException(status_code=403, detail="User Deleted, Not authorized")
    return user_db

@router.post("/register")
async def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    user.user_role = 'Cliente'
    respuesta = create_user_sql(db, user)
    if respuesta:
        return {"mensaje":"usuario registrado con éxito"}
    