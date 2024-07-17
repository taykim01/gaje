from fastapi import FastAPI
from src.repository.party.create_party import router as create_party_router
from src.repository.party.read_party import router as read_party_router
from src.repository.party.update_party_member import router as update_party_member_router
from src.repository.party.update_party_name import router as update_party_name_router

app = FastAPI()

@app.get("/")
def read_root():
    print("Welcome to the Trade Backend")
    return {"message": "Welcome to the Trade Backend"}

app.include_router(create_party_router)
app.include_router(read_party_router)
app.include_router(update_party_member_router)
app.include_router(update_party_name_router)