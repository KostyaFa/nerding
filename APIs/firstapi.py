from fastapi import FastAPI

app = FastAPI()


## просто вывод

@app.get('/user/{id}')
async def read_id(id: int):
    return {'user_id' : id}