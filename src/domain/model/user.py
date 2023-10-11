# from database_model import IDatabaseModel
from domain.model.database_model import IDatabaseModel

class User(IDatabaseModel):
    name: str
    age: int
    email: str
    document: str

    def __init__(self, name: str, age: int, email: str, document: str):
        super().__init__()
        self.name = name
        self.age = age
        self.email = email
        self.document = document

    def to_dict(self):
        return dict(
            _id = self._id,
            created_at = str(self.created_at),
            updated_at = str(self.created_at),
            email = self.email,
            name = self.name,
            age = self.age,
            document = self.document)
