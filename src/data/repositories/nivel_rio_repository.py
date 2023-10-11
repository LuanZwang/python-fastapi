from domain.model.database_model import IDatabaseModel
from data.base.base_repository import BaseRepository

class NivelRioRepository(BaseRepository):
    def __init__(self):
        super().__init__('nivel_rio')
