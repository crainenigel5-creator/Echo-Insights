from sqlalchemy import Column, Integer, String
from database.connection import Base


class ReviewDB(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    review_text = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)