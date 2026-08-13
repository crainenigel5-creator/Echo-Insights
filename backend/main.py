from fastapi import FastAPI

app = FastAPI(title="Echo Insights API")


@app.get("/")
def home():
    return {"message": "Echo Insights API is running!"}