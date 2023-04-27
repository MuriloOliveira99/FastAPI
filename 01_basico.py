from fastapi import FastAPI


'''
# doc da minha API
# http://127.0.0.1:8000/redoc ou doc

# end points
# POST
# GET
# PUT
# DELETE
# OPTIONS
# HEAD
# PATCH
# TRACE

# def vs async def
 a principal diferença entre def e async def é que as funções regulares são síncronas 
 e bloqueiam a execução do programa, enquanto as funções assíncronas são assíncronas e 
 permitem que o programa prossiga com outras tarefas enquanto aguarda 
 a conclusão de uma tarefa assíncrona.
'''

# instancia do FastAPI
app = FastAPI()

# end points
@app.get('/')
async def ola_mundo():
    return {'message': 'Hello World!'}


# endpoint com parametro e tipo de dado
@app.get('/itens/{item_id}')
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get('/users/me')
async def read_user_me():
    return {"user_id": "the current user"}

@app.get('/user/{user_id}')
async def read_user(user_id: int):
    return {"user_id": user_id}


