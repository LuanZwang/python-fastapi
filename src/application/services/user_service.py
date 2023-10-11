from data.repositories.user_repository import UserRepository
from domain.model.user import User

def getUser():
    return { 'data': { 'name': 'my_username' } }

def insert_user(user: User):
    userRepository = UserRepository()

    # lógica

    return userRepository.upsert(user)