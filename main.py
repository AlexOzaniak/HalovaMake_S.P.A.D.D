from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def test():
    return {"message": "choluj je randomak"}

# @app.post("/test/")