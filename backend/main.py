from fastapi import FastAPI
from routers import reviews
app = FastAPI(title="Echo Insights API")
app.include_router(reviews.router)




@app.get("/")
def home():
    return {"message": "Echo Insights API is running!"}