from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.review import Review
from database.connection import get_db
from database.models import ReviewDB


router = APIRouter(
    prefix="/reviews",
    tags=["Reviews"]
)


@router.get("/")
def get_reviews(db: Session = Depends(get_db)):
    reviews = db.query(ReviewDB).all()

    return reviews


@router.post("/")
def create_review(review: Review, db: Session = Depends(get_db)):
    new_review = ReviewDB(
        review_text=review.review_text,
        rating=review.rating
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return {
        "message": "Review saved successfully!",
        "review": {
            "id": new_review.id,
            "review_text": new_review.review_text,
            "rating": new_review.rating
        }
    }