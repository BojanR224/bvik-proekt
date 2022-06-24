import string
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from aleph_client.synchronous import create_aggregate, get_messages

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]




app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your todo list."}

@app.get("/v1/{id}")
async def list_all_messages(id: str):
    aggregate = await get_messages()
    return aggregate



# button 
# function
# create_aggreate
# 