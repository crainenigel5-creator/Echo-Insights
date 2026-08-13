from fastapi import APIRouter
from models.review import Review
router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)

@router.get("/")
def get_reviews():
    return {"message": "Echo Insights reviews endpoint is working!"}
@router.post("/")
def create_review(review: Review):
    return {
        "message": "Review received successfully!",
        "review": review
    }