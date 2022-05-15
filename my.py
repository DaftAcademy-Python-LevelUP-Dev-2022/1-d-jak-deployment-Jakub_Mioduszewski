from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def root():
    return {"start":"1970-01-01"}

@app.get("/method",status_code=200)
def root():
    return {"method":"GET"}
@app.put("/method",status_code=200)
def root():
    return {"method":"PUT"}
@app.options("/method",status_code=200)
def root():
    return {"method":"OPTIONS"}
@app.delete("/method",status_code=200)
def root():
    return {"method":"DELETE"}
@app.post("/method",status_code=201)
def root():
    return {"method":"POST"}
from fastapi import Response,status
days = {'monday':1,'tuesday':2,'wednesday':3,'thursday':4,'friday':5,'saturday':6,'sunday':7}
@app.get('/day/',status_code=400)
def name_and_number(name: str, number: int, response:Response):

    if number == days[name]:
        response.status_code = status.HTTP_200_OK
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST
    return response.status_code
from pydantic import BaseModel
class Calendar_In(BaseModel):

    date: str = None
    name: str = None
class Calendar_Out(BaseModel):
    id: int = 0
    name: str = None
    date: str = None
    date_added: str = None
import datetime
@app.put('/event',response_model=Calendar_Out)
def create_calendar(item: Calendar_In):
    item_dict = item.dict()
    out_dict = Calendar_Out.dict()
    out_dict.update(({'id':id + 1}))
    out_dict.upadate({'name':item_dict.name})
    out_dict.update({'date':item_dict.date})

    date_now = datetime.date(datetime.now())
    out_dict.update({"date_added":date_now})
    return out_dict
