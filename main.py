from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "This is your post"}

@app.post("/create_posts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']}, content: {payload['content']}"}