from data.base.base_repository import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__('users')
        self.create_indexes()

    def create_indexes(self):
        self.collection.create_index('email', unique=True)
        self.collection.create_index('document', unique=True)