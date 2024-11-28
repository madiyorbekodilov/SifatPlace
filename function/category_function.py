from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from models import Category, Product
from dtos import CategoryCreate, CategoryResult, CategoryUpdate

async def create_category(category: CategoryCreate, db):
    db_category = await db.query(Category).filter(Category.name == category.name).first()
    if db_category is not None:
        raise HTTPException(status_code=403, detail="Category already exists")

    new_category = Category(
        name=category.name
    )
    db.add(new_category)
    db.commit()
    return CategoryResult(
        name=category.name,
        subcategories=None
    )

async def update_category(category: CategoryUpdate, db):
    db_category = await db.query(Category).filter(Category.id == category.id).first()
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    if category.name is not None:
        db_category.name = category.name

    db.commit()
    db.refresh(db_category)
    return True

async def delete_category(category_id: int, db):
    db_category = await db.query(Category).filter(Category.id == category_id).first()

    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(db_category)
    db.commit()
    return True


async def get_category(category_id: int, db):
    db_category = await db.query(Category).options(joinedload(Product.subcategory)).filter(Category.id == category_id).first()

    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return CategoryResult(
        name=db_category.name,
        subcategories=db_category.subcategories
    )

async def get_all_categories(db):
    db_categories = await db.query(Category).options(joinedload(Product.subcategory)).all()

    all_categories = []

    if db_categories is None:
        raise HTTPException(status_code=404, detail="Category not found")

    for category in db_categories:
        all_categories.append(CategoryResult(
            name=category.name,
            subcategories=category.subcategories
        ))

    return all_categories
