from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_history():
    return {"message": "History endpoint coming after PostgreSQL integration"}