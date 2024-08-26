from fastapi import FastAPI
from Models.PostModel import Post

# Initialize the server
app = FastAPI()


# Welcome to the API
@app.get("/api/")
async def root():
    return {"message": "Hello From FastAPI!!"}


# Get Posts Method
@app.get("/api/posts/")
async def get_posts():
    return {
        "data": {
            "title": "Hello From FastAPI",
            "description": "This is a social media API built using FastAPI!!",
        }
    }


# Create the post Method
@app.post("/api/posts/")
async def create_post(post: Post):
    print(post.title)
    print(post.content)

    return {"message": "Create a new post"}
