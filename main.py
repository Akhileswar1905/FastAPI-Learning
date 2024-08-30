from fastapi import FastAPI, HTTPException, status
from Models.PostModel import Post
import psycopg2
from psycopg2.extras import RealDictCursor
import time

# Initialize the server
app = FastAPI()

while True:
    try:
        con = psycopg2.connect(
            host="localhost",
            database="FastAPI",
            user="postgres",
            password="Password",
            cursor_factory=RealDictCursor,
        )

        cur = con.cursor()
        print("DB Connected Successfully")
        con.commit()
        break
    except Exception as e:
        print(e)
        time.sleep(2)


# Welcome to the API
@app.get("/api/")
async def root():
    return {"message": "Hello From FastAPI!!"}


# Get Posts Method
@app.get("/api/posts/")
async def get_posts():
    cur.execute("""select * from posts order by id;""")
    posts = cur.fetchall()
    con.commit()
    return {"data": posts}


# Create the post Method
@app.post("/api/posts/", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    cur.execute(
        """insert into posts (title, content, published) values (%s, %s, %s) returning *;""",
        (post.title, post.content, post.published),
    )
    new_post = cur.fetchone()
    con.commit()

    return {"new post": new_post}


# Get a post by id
@app.get("/api/posts/{id}", status_code=status.HTTP_200_OK)
async def get_post(id: int):
    id = str(id)
    cur.execute("""select * from posts where id = %s;""", (id,))
    post = cur.fetchone()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return {"data": post}


# Delete a post
@app.delete("/api/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    try:
        cur.execute(
            """
            delete from posts where id = %s returning *;
        """,
            (str(id)),
        )
        dlt_post = cur.fetchone()
        con.commit()
        print(dlt_post)
        if not dlt_post:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
            )
        return {"data": dlt_post}
    except Exception as e:
        return {"error": e}


# Update a post
@app.put("/api/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_post(id: int, update: Post):
    id = str(id)
    cur.execute(
        """
        update posts set title = %s, content = %s, published = %s where id = %s returning *;
    """,
        (update.title, update.content, update.published, id),
    )
    post = cur.fetchone()
    con.commit()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return {"data": post}
