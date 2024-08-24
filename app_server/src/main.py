from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    print("i got called!")
    return {"message": "Hello World"}


@app.get("/endpoint")
async def endpoint():
    print("endpoint called")
    return {"message": "endpoint"}