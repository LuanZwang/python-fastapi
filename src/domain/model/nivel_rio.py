import datetime
import json
from domain.model.database_model import IDatabaseModel

class NivelRio(IDatabaseModel):
    niveis: list

    def __init__(self, niveis): 
        super().__init__()
        self.niveis = niveis

    def to_dict(self):
        return dict(
            _id = self._id,
            created_at = str(self.created_at),
            updated_at = str(self.updated_at),
            niveis = self.niveis)

    def to_json(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=4)

class Nivel:
    nivel: float
    horaLeitura: datetime