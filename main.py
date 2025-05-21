from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: float = None

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "This is your post"}

@app.post("/createposts")
def create_posts(post: Post):
    post_dict = post.dict()
    print(post_dict)
    return {"data": post, "message": "Post created successfully"}