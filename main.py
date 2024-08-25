from fastapi import FastAPI

# Initialize the server
app = FastAPI()


# Welcome to the API
@app.get("/api/")
async def root():
    return {"message": "Hello From FastAPI!!"}


# Get Posts Method
@app.get("/api/posts")
async def get_posts():
    return {
        "data": {
            "title": "Hello From FastAPI",
            "description": "This is a social media API built using FastAPI!!",
        }
    }
