from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
def login():
    return {"message": "Auth system coming with PostgreSQL + JWT"}