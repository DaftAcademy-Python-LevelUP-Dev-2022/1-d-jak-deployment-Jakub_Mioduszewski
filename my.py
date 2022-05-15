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
class Calendar(BaseModel):

    event: str
    date: str
import datetime
@app.put('/event')
def create_calendar(item: Calendar):
    item_dict = item.dict()
    if item.event:
        date_now = datetime.date(datetime.now())
        item_dict.update({"date_added":date_now})
    return item_dict
