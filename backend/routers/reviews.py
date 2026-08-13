from fastapi import APIRouter

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)

@router.get("/")
def get_reviews():
    return {"message": "Echo Insights reviews endpoint is working!"}