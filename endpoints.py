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

    @app.put("/update/user/{id}")
    async def user_update(user: UserUpdate, db: Session = Depends(get_db)):
        response = await update_user(user,db)
        return {
            "message": "user successfully updated",
            "statusCode": 200,
            "data": response
        }

    @app.delete("/delete/user/{id}")
    async def user_delete(user_id: int, db: Session = Depends(get_db)):
        response = await delete_user(user_id,db)
        return {
            "message": "user successfully deleted",
            "statusCode": 200,
            "data": response
        }

    @app.get("/get/user/{id}")
    async def user_get(user_id: int, db: Session = Depends(get_db)):
        response = await get_user_by_id(user_id,db)
        return {
            "message": "user successfully retrieved",
            "statusCode": 200,
            "data": response
        }