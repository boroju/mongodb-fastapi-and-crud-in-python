from fastapi import APIRouter, status, Response
from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT

from models.user import User
from config.database import collection_users
from schemas.user import user_entity, users_entity

user = APIRouter()


@user.get('/users', response_model=list[User], tags=["users"])
async def find_all_users():
    # print(list(collection_users.find()))
    return users_entity(collection_users.find())


@user.post('/users', response_model=User, tags=["users"])
async def create_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    del new_user["id"]
    id = collection_users.insert_one(new_user).inserted_id
    user = collection_users.find_one({"_id": id})
    return user_entity(user)


@user.get('/users/{id}', response_model=User, tags=["users"])
async def find_user(id: str):
    return user_entity(collection_users.find_one({"_id": ObjectId(id)}))


@user.put("/users/{id}", response_model=User, tags=["users"])
async def update_user(id: str, user: User):
    collection_users.find_one_and_update({
        "_id": ObjectId(id)
    }, {
        "$set": dict(user)
    })
    return user_entity(collection_users.find_one({"_id": ObjectId(id)}))


@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
async def delete_user(id: str):
    collection_users.find_one_and_delete({
        "_id": ObjectId(id)
    })
    return Response(status_code=HTTP_204_NO_CONTENT)
