from fastapi import FastAPI

from appv1.routers import users

from appv1.routers import roles
from appv1.routers import categories
from appv1.routers import login

from appv1.schemas.user import UserCreate
from appv1.schemas.rol import RolCreate
from appv1.schemas.category import CategoryCreate
from core.security import get_hashed_password, verify_password, create_access_token
from db.database import test_db_connection

# mypass = '12345'
# otropass = '12345'


app = FastAPI()
app.include_router(users.router, tags=["users"])
app.include_router(roles.router, tags=["roles"])
app.include_router(categories.router, tags=["categories"])
app.include_router(login.router, prefix="/access", tags=["access"])
@app.on_event("startup")
def on_startup():
    test_db_connection()

# pass_has1 = get_hashed_password(mypass)
# pass_has2 = get_hashed_password(otropass)

# resultado = verify_password(otropass, pass_has1)
# datadic ={"user_id":234234, "rol":"Admin"}

# if resultado ==True:
#     tokenjwt = create_access_token(datadic)
# else:
#     tokenjwt = "invalido"    

# tokenjwt = create_access_token(datadic)



@app.get("/")
async def read_root():
    return {
        
            "Hello": "World",
           
            }

