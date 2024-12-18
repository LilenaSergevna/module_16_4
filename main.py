from fastapi import FastAPI, Path, HTTPException
import uvicorn
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id : int
    username : str
    age : int


users = []

@app.get("/")
async def read_root():
    return {"Главная страница"}


@app.get("/users")
async def read_user_all():
    return users

@app.post('/user/{username}/{age}')
async def create_user(username, age):
    print(len(users))
    new_id = len(users) + 1
    new_user=User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int,username, age):
    print(f'{user_id},{username},{age}')
    for user in users:
        print(f'{user.id}, {user_id}')
        if user.id == user_id:
            user.username=username
            user.age=age
            return user
    raise HTTPException(status_code=404, detail="Задача не найдена")

@app.delete('/user/{user_id}')
async def delete_user(user_id:int):

    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="Задача не найдена")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8005)