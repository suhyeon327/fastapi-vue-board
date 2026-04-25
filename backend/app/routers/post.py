# filename: backend/app/routers/post.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.post import Post
from app.schemas.post import PostCreate, PostResponse

router = APIRouter(prefix="/posts", tags=["게시글"])

@router.get("/", summary="게시글 목록")
def list_posts(
    page: int = 1,
    size: int = 10,
    db: Session = Depends(get_db),
) -> list[PostResponse]:
    offset = (page - 1) * size
    posts = (
        db.query(Post)
        .order_by(Post.created_at.desc())
        .offset(offset)
        .limit(size)
        .all()
    )
    return posts


@router.post("/", summary="게시글 생성", status_code=201)
def create_post(
    post: PostCreate, db: Session = Depends(get_db)
) -> PostResponse:
    new_post = Post(title=post.title, content=post.content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{post_id}", summary="게시글 상세")
def get_post(
    post_id: int, db: Session = Depends(get_db)
) -> PostResponse:
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=404, detail="게시글을 찾을 수 없습니다"
        )
    return post


@router.put("/{post_id}", summary="게시글 수정")
def update_post(
    post_id: int,
    post_data: PostCreate,
    db: Session = Depends(get_db),
) -> PostResponse:
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=404, detail="게시글을 찾을 수 없습니다"
        )
    post.title = post_data.title
    post.content = post_data.content
    db.commit()
    db.refresh(post)
    return post


@router.delete("/{post_id}", summary="게시글 삭제", status_code=204)
def delete_post(
    post_id: int, db: Session = Depends(get_db)
):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=404, detail="게시글을 찾을 수 없습니다"
        )
    db.delete(post)
    db.commit()