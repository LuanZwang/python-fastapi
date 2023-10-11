# from ...data.repositories import user_repository
from data.repositories.nivel_rio_repository import NivelRioRepository
from domain.model.nivel_rio import NivelRio
from shared.utils import str_utils

def get_by_id(id: str):
    if (str_utils.isNullOrWhiteSpace(id)):
        return { 'message': 'not found' }

def insert_nivelRio(nivelRio: NivelRio, id: str =None) -> dict:
    nivelRioRepository = NivelRioRepository()
    notNullId = not str_utils.isNullOrWhiteSpace(id)
    
    if (notNullId):
        nivelRio._id = id

    return nivelRioRepository.upsert(nivelRio, notNullId)