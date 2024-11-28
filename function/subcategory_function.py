from fastapi import HTTPException
from sqlalchemy.orm import joinedload

from models import SubCategory, Category
from dtos import SubcategoryResult, SubcategoryCreate, SubcategoryUpdate

async def create_subcategory(subcategory: SubcategoryCreate, db):
    db_subcategory = await db.query(SubCategory).filter(SubCategory.name == subcategory.name).first()

    if db_subcategory is not None:
        raise HTTPException(status_code=400, detail='Subcategory already exists')


    category_id = await db.query(Category).filter(Category.name == subcategory.name).first().id
    new_subcategory = SubCategory(
        name=subcategory.name,
        category_id=category_id
    )

    await db.add(new_subcategory)
    await db.commit()
    return SubcategoryResult(
        name=new_subcategory.name,
        products=None
    )

async def update_subcategory(subcategory: SubcategoryUpdate, db):
    db_subcategory = await db.query(SubCategory).filter(SubCategory.id == subcategory.id).first()
    if db_subcategory is None:
        raise HTTPException(status_code=404, detail='Subcategory not found')

    if subcategory.name is not None:
        db_subcategory.name = subcategory.name

    if subcategory.category_name is not None:
        category_id = await db.query(Category).filter(Category.name == subcategory.name).first().id
        if category_id is None:
            raise HTTPException(status_code=404, detail='Category not found')
        db_subcategory.category_id = category_id

    db.commit()
    db.refresh(db_subcategory)
    return True

async def delete_subcategory(subcategory_id: int, db):
    db_subcategory = await db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()

    if db_subcategory is None:
        raise HTTPException(status_code=404, detail='Subcategory not found')

    db.delete(db_subcategory)
    db.commit()
    return True

async def get_subcategories(subcategory_id: int, db):
    db_subcategory = await db.query(SubCategory).options(joinedload(SubCategory.products)).filter(SubCategory.id == subcategory_id).first()

    if db_subcategory is None:
        raise HTTPException(status_code=404, detail='Subcategory not found')

    return SubcategoryResult(
        name=db_subcategory.name,
        products=db_subcategory.products
    )
