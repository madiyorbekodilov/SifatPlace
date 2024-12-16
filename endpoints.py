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

    # Category
    @app.post("/create/category")
    async def category_create(category: CategoryCreate, db: Session = Depends(get_db)):
        response = await create_category(category,db)
        return {
            "message": "category successfully created",
            "statusCode": 200,
            "data": response
        }

    @app.put("/update/category")
    async def category_update(category: CategoryUpdate, db: Session = Depends(get_db)):
        response = await update_category(category,db)
        return {
            "message": "category successfully updated",
            "statusCode": 200,
            "data": response
        }

    @app.delete("/delete/category/{id}")
    async def category_delete(category_id: int, db: Session = Depends(get_db)):
        response = await delete_category(category_id,db)
        return {
            "message": "category successfully deleted",
            "statusCode": 200,
            "data": response
        }

    @app.get("/get/category/{id}")
    async def category_get(category_id: int, db: Session = Depends(get_db)):
        response = await get_category(category_id,db)
        return {
            "message": "category successfully retrieved",
            "statusCode": 200,
            "data": response
        }

    @app.get("/get-all/category")
    async def category_get_all(db: Session = Depends(get_db)):
        response = await get_all_categories(db)
        return {
            "message": "category successfully retrieved",
            "statusCode": 200,
            "data": response
        }

    # Subcategory
    @app.post("/create/subcategory")
    async def subcategory_create(subcategory: SubcategoryCreate, db: Session = Depends(get_db)):
        response = await create_subcategory(subcategory,db)
        return {
            "message": "subcategory successfully created",
            "statusCode": 200,
            "data": response
        }

    @app.put("/update/subcategory")
    async def subcategory_update(subcategory: SubcategoryUpdate, db: Session = Depends(get_db)):
        response = await update_subcategory(subcategory,db)
        return {
            "message": "subcategory successfully updated",
            "statusCode": 200,
            "data": response
        }

    @app.delete("/delete/subcategory/{id}")
    async def subcategory_delete(subcategory_id: int, db: Session = Depends(get_db)):
        response = await delete_category(subcategory_id,db)
        return {
            "message": "subcategory successfully deleted",
            "statusCode": 200,
            "data": response
        }

    @app.get("/get/subcategory/{id}")
    async def subcategory_get(subcategory_id: int, db: Session = Depends(get_db)):
        response = await get_subcategories(subcategory_id,db)
        return {
            "message": "subcategory successfully retrieved",
            "statusCode": 200,
            "data": response
        }

    # Product
    @app.post("/create/product")
    async def product_create(product: ProductCreate, db: Session = Depends(get_db)):
        response = await create_product(product,db)
        return {
            "message": "product successfully created",
            "statusCode": 200,
            "data": response
        }

    @app.put("/update/product")
    async def product_update(product: ProductUpdate, db: Session = Depends(get_db)):
        response = await update_product(product,db)
        return {
            "message": "product successfully updated",
            "statusCode": 200,
            "data": response
        }

    @app.delete("/delete/product/{id}")
    async def product_delete(product_id: int, db: Session = Depends(get_db)):
        response = await delete_product(product_id,db)
        return {
            "message": "product successfully deleted",
            "statusCode": 200,
            "data": response
        }

    @app.get("/get/product/{id}")
    async def product_get(product_id: int, db: Session = Depends(get_db)):
        response = await get_product(product_id,db)
        return {
            "message": "product successfully retrieved",
            "statusCode": 200,
            "data": response
        }

    # Comment
    @app.post("/create/comment")
    async def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
        response = await comment_create(comment,db)
        return {
            "message": "comment successfully created",
            "statusCode": 200,
            "data": response
        }

    @app.put("/update/comment")
    async def update_comment(comment: CommentUpdate, db: Session = Depends(get_db)):
        response = await comment_update(comment,db)
        return {
            "message": "comment successfully updated",
            "statusCode": 200,
            "data": response
        }

    @app.delete("/delete/comment/{id}")
    async def delete_comment(comment_id: int, db: Session = Depends(get_db)):
        response = await comment_delete(comment_id,db)
        return {
            "message": "comment successfully deleted",
            "statusCode": 200,
            "data": response
        }

    # Location
    @app.post("/create/location")
    async def create_location(location: LocationCreate, db: Session = Depends(get_db)):
        response = await location_create(location,db)
        return {
            "message": "location successfully created",
            "statusCode": 200,
            "data": response
        }

    @app.put("/update/location")
    async def update_location(location: LocationUpdate, db: Session = Depends(get_db)):
        response = await location_update(location,db)
        return {
            "message": "location successfully updated",
            "statusCode": 200,
            "data": response
        }

    @app.delete("/delete/location/{id}")
    async def delete_location(location_id: int, db: Session = Depends(get_db)):
        response = await location_delete(location_id,db)
        return {
            "message": "location successfully deleted",
            "statusCode": 200,
            "data": response
        }