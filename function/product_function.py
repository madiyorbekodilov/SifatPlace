from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from models import Product, SubCategory
from dtos import ProductResult, ProductUpdate, ProductCreate

async def create_product(product: ProductCreate, db):
    db_product = db.query(Product).filter(Product.name == product.name).first()
    if db_product is not None:
        raise HTTPException(status_code=403, detail="Product already exists")
    subcategory_idd = db.query(SubCategory).filter(SubCategory.name == product.sub_category).first().id
    new_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        futures=product.futures,
        subcategory_id=subcategory_idd,
    )

    db.add(new_product)
    db.commit()
    return ProductResult(
        name=new_product.name,
        description=new_product.description,
        price=new_product.price,
        futures=new_product.futures,
        comments=None
    )

async def update_product(product: ProductUpdate, db):
    db_product = db.query(Product).filter(Product.id == product.id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.sub_category is not None:
        subcategory_idd = db.query(SubCategory).filter(SubCategory.name == product.sub_category).first().id
        if subcategory_idd is None:
            raise HTTPException(status_code=404, detail="SubCategory not found")
        db_product.subcategory_id = subcategory_idd

    if product.name is not None:
        db_product.name = product.name

    if product.description is not None:
        db_product.description = product.description

    if product.price is not None:
        db_product.price = product.price

    if product.futures is not None:
        db_product.futures = product.futures

    db.commit()
    db.refresh(db_product)
    return ProductResult(
        name=db_product.name,
        description=db_product.description,
        price=db_product.price,
        futures=db_product.futures,
        comments=None
    )

async def delete_product(product_id: int, db):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(db_product)
    db.commit()
    return True

async def get_product(product_id: int, db):
    db_product = db.query(Product).option(joinedload(Product.comment)).filter(Product.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    return ProductResult(
        name=db_product.name,
        description=db_product.description,
        price=db_product.price,
        futures=db_product.futures,
        comments=db_product.comments
    )
