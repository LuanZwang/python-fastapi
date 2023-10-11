from pydantic import BaseModel
from domain.model.user import User

class AddUserDto(BaseModel):
    name: str
    age: int
    email: str
    document: str

    def to_domain(self):
        return User(
            self.name,
            self.age,
            self.email,
            self.document)