from datetime import datetime

from fastapi import HTTPException
from models import Comment
from dtos import CommentResult, CommentCreate, CommentUpdate

async def comment_create(comment: CommentCreate, db):
    new_comment = Comment(
        writer_name=comment.writer_name,
        star=comment.star,
        like=comment.like,
        unlike=comment.unlike,
        date=datetime.now(),
        product_id=comment.product_id
    )

    db.add(new_comment)
    db.commit()
    return CommentResult(
        writer_name=new_comment.writer_name,
        star=new_comment.star,
        like=new_comment.like,
        unlike=new_comment.unlike,
        date=new_comment.date,
    )

async def comment_update(comment: CommentUpdate, db):
    db_comment = db.query(Comment).filter(Comment.id == comment.id).first()

    if db_comment is None:
        raise HTTPException(status_code=404, detail="comment not found")

    if comment.like is not None:
        db_comment.like = comment.like
    if comment.unlike is not None:
        db_comment.unlike = comment.unlike
    if comment.star is not None:
        db_comment.star = comment.star

    db.commit()
    db.refresh(db_comment)
    return True

async def comment_delete(comment_id: int, db):
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if db_comment is None:
        raise HTTPException(status_code=404, detail="comment not found")

    db.delete(db_comment)
    db.commit()
    return True