from utility import ofline_route
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn 
import json 
from typing import List 

app = FastAPI()

class base(BaseModel):
        graph : str
        start : List
        end : List

@app.post('/offline_route')
def route(req:base):

    req_dict = req.dict()
    graph = req_dict['graph']
    start = req_dict['start']
    end = req_dict['end']

    result = ofline_route(graph=graph,start_point=start,end_point=end)
    result.read_graph()
    
    return {'Route':result.create_route()}


if __name__ == '__main__' :
      uvicorn.run(app=app,host='127.0.0.1',port=8000)