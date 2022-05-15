import datetime

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
from datetime import datetime
event = {
    "id":-1, 'name': None, 'date': None, 'date_added': 0

}
class CalendarIn(BaseModel):
    date: str
    event: str
class CalendarOut(BaseModel):
    id: int = 0
    name: str
    date: str
    date_added: str
@app.put("/event",response_model=CalendarOut)
def calendar(item: CalendarIn,response: Response):
    new_id = event['id'] + 1
    day = datetime.date(datetime.now()).isoformat()
    event.update({"id":new_id, "name":item.event,"date":item.date,'date_added':day})
    return event, status.HTTP_200_OK
