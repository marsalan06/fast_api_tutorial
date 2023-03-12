from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':"Arsalan"}}



@app.get('/about')
def about():
    return {'data':'about page'}


@app.get('/blog/complete')
def complete():
    return {'data':'blog route without type issue'}

@app.get('/blog/{id}') #dynamic url
def index(id: int): #fix the type by adding id: int 
    return {'data':'blog list '+ str(id)}

@app.get('/query')
def query_method(number,published: Optional[bool]=True): #so now number is required but published is optional and has a default value
    #http://127.0.0.1:8000/query?number=3&published=true
    if published:
        return {"returning all data":f"{number}"}
    #http://127.0.0.1:8000/query?number=3&published=false
    else:
        return {"returning some data":f"{number}"}

