import json
from typing import Optional, Union, List, Dict, Any
from fastapi import FastAPI
from pydantic import BaseModel
# python -m uvicorn api:app --reload

# serializados de saida
# toda vez q entregamos algo para alguem
# colocamos Out no nome da classe como uma boa pratica
class PersonOut(BaseModel):
    id: int
    name: str
    picture: str
    age: int
    email: str
    about: Optional[str] = 'Valor default'
    is_active: bool

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"name": "Murilo"}

@app.get("/person")
async def person(): #responde_model = PersonOut
    return PersonOut(
        id = 1,
        name = "Murilo",
        picture = "www.photoapi.com.br",
        age = 60,
        email = "murilo123@hotmail.com",
        about = "Retornando um objeto do tipo Person",
        is_active = True 
    )

    # usando dict ao invés de classe
    # colocar "responde_model = PersonOut" no parametro da funcao
    # valida se o dicionario ele esta de acordo com o PersonOut
    # return dict(
    #     id = 1,
    #     name = "Murilo",
    #     picture = "www.photoapi.com.br",
    #     age = 60,
    #     email = "murilo123@hotmail.com",
    #     about = "Retornando um objeto do tipo Person",
    #     is_active = True 
    # )


@app.get("/varias_person", response_model = List[PersonOut])
async def varias_person(): 
    return pessoas()


def pessoas(is_active = None) -> List[Dict[str, Any]]:
    with open('data.json') as datafile:
        data = json.loads(datafile.read())

    if is_active is not None:
        return [
            pessoa for pessoa in data
            if pessoa['is_active'] == is_active
        ]
    return data