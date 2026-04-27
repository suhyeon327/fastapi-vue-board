# filename: backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.models.post import Post  # noqa: F401
from app.routers import post as post_router

# 데이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="게시판 API",
    description="FastAPI와 Vue.js로 만드는 게시판 서비스",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://fastapi-vue-board-delta.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(post_router.router)


@app.get("/")
def health_check():
    return {"status": "ok"}