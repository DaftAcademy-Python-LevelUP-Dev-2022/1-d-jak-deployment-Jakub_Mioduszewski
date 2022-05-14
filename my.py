from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def root():
    return {"start":"1970-01-01"}

@app.get("/method")
def root():
    return {"method":"GET"}
@app.put("/method")
def root():
    return {"method":"PUT"}
@app.options("/method")
def root():
    return {"method":"OPTIONS"}
@app.delete("/method")
def root():
    return {"method":"DELETE"}
@app.post("/method")
def root():
    return {"method":"POST"}
