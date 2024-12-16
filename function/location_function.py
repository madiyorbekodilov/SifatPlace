
from fastapi import HTTPException
from models import Comment, Location
from dtos import CommentResult, CommentCreate, CommentUpdate, LocationCreate, LocationResult, LocationUpdate
from datetime import datetime

async def location_create(location: LocationCreate, db):
    new_comment = Location(
        name=location.name,
        longitude=location.longitude,
        latitude=location.latitude,
        user_id=location.user_id,
    )

    db.add(new_comment)
    db.commit()
    return LocationResult(
        name=new_comment.name,
        longitude=new_comment.longitude,
        latitude=new_comment.latitude
    )

async def location_update(location: LocationUpdate, db):
    db_comment = db.query(Location).filter(Location.id == location.id).first()

    if db_comment is None:
        raise HTTPException(status_code=404, detail="comment not found")

    if location.name is not None:
        db_comment.name = location.name
    if location.longitude is not None:
        db_comment.longitude = location.longitude
    if location.latitude is not None:
        db_comment.latitude = location.latitude

    db.commit()
    db.refresh(db_comment)
    return True

async def location_delete(location_id: int, db):
    db_comment = db.query(Location).filter(Location.id == location_id).first()
    if db_comment is None:
        raise HTTPException(status_code=404, detail="comment not found")

    db.delete(db_comment)
    db.commit()
    return True