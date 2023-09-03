from fastapi import FastAPI, HTTPException
from humancat import human, cat

cats = {}
humans = {}

app = FastAPI()

@app.post('/cat/{name}')
def create_cat(name: str):
    cat_obj = cat.Cat(name)

    if name in cats:
        raise HTTPException(status_code=409, detail=f'Cat {name} already exists')
    else:
        cats[name] = cat_obj
        return {'name': name}

@app.get('/cat/{name}')
def get_cat(name: str):
    if name in cats:
        return {'name': name, 'status': cats[name].get_status()}
    else:
        raise HTTPException(status_code=404, detail=f'Cat {name} not found')

@app.get('/cat/{name}/status')
def get_cat_status(name: str):
    if name in cats:
        return {'status': cats[name].get_status()}
    else:
        raise HTTPException(status_code=404, detail=f'Cat {name} not found')

@app.put('/cat/{name}/status/{status}')
def set_cat_status(name: str, status: str):
    if name in cats:
        cats[name].set_status(status)
        return {'name': name, 'status': cats[name].get_status()}
    else:
        raise HTTPException(status_code=404, detail=f'Cat {name} not found')

@app.post('/cat/{name}/meow')
def cat_meow(name: str):
    if name in cats:
        return {'meow': cats[name].meow()}
    else:
        raise HTTPException(status_code=404, detail=f'Cat {name} not found')

@app.delete('/cat/{name}')
def dead_cat(name: str):
    if name in cats:
        del cats[name]
        return {'message': f'Cat {name} is dead'}
    else:
        raise HTTPException(status_code=404, detail=f'Cat {name} not found')

@app.post('/human/{name}')
def create_human(name: str):
    human_obj = human.Human(name)

    if name in humans:
        raise HTTPException(status_code=409, detail=f'Human {name} already exists')
    else:
        humans[name] = human_obj
        return {'name': name}
    
@app.get('/human/{name}')
def get_human(name: str):
    if name in humans:
        return {'name': name, 'age': humans[name].get_age(), 'message': humans[name].get_info()}
    else:
        raise HTTPException(status_code=404, detail=f'Human {name} not found')
    
@app.get('/human/{name}/age')
def get_human_age(name: str):
    if name in humans:
        return {'age': humans[name].get_age()}
    else:
        raise HTTPException(status_code=404, detail=f'Human {name} not found')
    
@app.put('/human/{name}/age/{age}')
def set_human_age(name: str, age: int):
    if name in humans:
        humans[name].set_age(age)
        return {'name': name, 'age': humans[name].get_age()}
    else:
        raise HTTPException(status_code=404, detail=f'Human {name} not found')

@app.delete('/human/{name}')
def dead_human(name: str):
    if name in humans:
        del humans[name]
        return {'message': f'Human {name} is dead'}
    else:
        raise HTTPException(status_code=404, detail=f'Human {name} not found')