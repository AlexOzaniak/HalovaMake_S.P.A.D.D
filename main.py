from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def test():
    return {"message": "choluj je zmrd"}

@app.post("/test/")
 