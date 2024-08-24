from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    print("i got called!")
    return {"message": "Hello World"}