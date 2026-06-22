from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI!s"}

# path parameters
@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}

# get current user
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"} 

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id} 

# creating list of users 
fake_users_db = [{'id': '001', 'name': 'user1'}, {'id': '002', 'name': 'user2'}, {'id': '003', 'name': 'user3'}]
@app.get("/users/")
async def read_users():
    return fake_users_db

@app.get("/users/{user_id}")
async def read_user2(user_id: int):
    return fake_users_db[user_id]   

@app.get("/animal_names")
async def get_animal_names():
    return ["dog", "cat", "rabbit", "hamster"]


 