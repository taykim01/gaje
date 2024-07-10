from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    print("Welcome to the Trade Backend")
    return {"message": "Welcome to the Trade Backend"}

