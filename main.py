from fastapi import FastAPI, HTTPException, status
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
    return {"data": posts}


# Create the post Method
posts = [
    {"title": "Post 1", "content": "This is post1", "id": 1},
    {"title": "Post 2", "content": "This is post2", "id": 2},
]


@app.post("/api/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    post = post.dict()
    post["id"] = len(posts) + 1
    posts.append(post)

    return {"new post": post}


# Get a post by id
@app.get("/api/posts/{id}", status_code=status.HTTP_200_OK)
async def get_post(id: int):
    for post in posts:
        if post["id"] == id:
            return {"data": post}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


# Delete a post
@app.delete("/api/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    for post in posts:
        if post["id"] == id:
            posts.remove(post)
            return {"message": "Post deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


# Update a post
@app.put("/api/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_post(id: int, update: Post):
    for post in posts:
        if post["id"] == id:
            p = update.dict()
            p["id"] = id
            posts.remove(post)
            posts.append(p)
            return {"message": "Post updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
