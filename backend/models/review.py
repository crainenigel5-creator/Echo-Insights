from pydantic import BaseModel, Field


class Review(BaseModel):
    review_text: str
    rating: int = Field(ge=1, le=5)