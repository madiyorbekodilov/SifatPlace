from fastapi import HTTPException
from dtos import *
from models import *
from helpers.passwordHelper import hash_password, verify_password

# User
async def create_user(user: UserCreate, db):
    db_query = db.query(User).filter(User.number == user.number).first()
    if db_query is not None:
        raise HTTPException(status_code=402, detail='User already exists')

    people = User(
        name= user.name,
        email= user.email,
        password= hash_password(user.password),
        number= user.number,
        brith_day= user.brith_day
    )

    db.add(people)
    db.commit()
    return UserResult(
        name=user.name,
        email=user.email,
        number=user.number,
        brith_day=user.brith_day
    )


async def update_user(user: UserUpdate, db):
    db_user = db.query(User).filter(User.id == user.id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='User does not exist')

    if user.name is not None:
        db_user.name = user.name

    if user.email is not None:
        db_user.email = user.email

    if user.brith_day is not None:
        db_user.brith_day = user.brith_day

    db.commit()
    db.refresh(db_user)
    return True

async def get_user_by_id(user_id: int, db):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='User does not exist')

    return UserResult(
        name=db_user.name,
        email=db_user.email,
        number=db_user.number,
        brith_day=db_user.brith_day
    )


async def delete_user(user_id: int, db):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='User does not exist')
    db.delete(db_user)
    db.commit()
    return True

