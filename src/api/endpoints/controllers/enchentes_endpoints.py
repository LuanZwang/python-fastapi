from fastapi import Body, Request, APIRouter
from pydantic import BaseModel
import datetime
import requests
import json
from domain.model.database_model import IDatabaseModel
from domain.model.nivel_rio import NivelRio
from application.services import nivel_rio_service

router = APIRouter()

#localhost/enchentes
@router.post("/enchentes/{id:path}")
async def read_users(id: str):
    try:
        request = requests.get('https://alertablu.blumenau.sc.gov.br/static/data/nivel_oficial.json', verify=False)
       
        return nivel_rio_service.insert_nivelRio(id, NivelRio(request.json()['niveis']))

        # return NivelRio(request.json()['niveis'])
    except Exception as e:
        print(e)