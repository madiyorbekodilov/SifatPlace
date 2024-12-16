from fastapi import Depends
from sqlalchemy.orm import Session

from function.functions import *
from function.comment_function import *
from function.product_function import *
from function.category_function import *
from function.location_function import *
from function.subcategory_function import *

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def total_endpoints(app):
    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    @app.get("/hello/{name}")
    async def say_hello(name: str):
        return {"message": f"Hello {name}"}

    # User
    @app.post("/create/user")
    async def user_create(user: UserCreate, db: Session = Depends(get_db)):
        response = await create_user(user,db)
        return {
            "message": "user successfully created",
            "statusCode": 200,
            "data": response
            }
