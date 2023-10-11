from fastapi import Body, Request, APIRouter
from pydantic import BaseModel
from api.endpoints.DTOs.user.add_user_dto import AddUserDto
from application.services import user_service

router = APIRouter()

@router.get("/users/")
async def read_users():
    return [{"username": "Foo"}, {"username": "Bar"}]

@router.post("/users/add-user")
async def add_user(user: AddUserDto):
    return user_service.insert_user(user.to_domain())
    # return user

# @router.post("/users/dummypath")
# async def dummy_path(payload: Request):
#     return await payload.body()