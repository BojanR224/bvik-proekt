import string
from coincurve import PrivateKey
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from aleph_client.synchronous import create_aggregate, get_messages
from aleph_client.chains.ethereum import ETHAccount

app = FastAPI()

private_key = bytes.fromhex("f12ee701be6699b7e597b1ce7a76b7cc82b0be6abb27007091403d3a50b72f01")

account = ETHAccount(private_key)

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
    aggregate_message = await create_aggregate(account, 'testKey',{'1':1}, channel='BViK-proekt')
    return {"message": aggregate_message}

# @app.get("/v1/{id}")
# async def list_all_messages(id: str):
#     aggregate = await get_messages()
#     return aggregate



# button 
# function
# create_aggreate
# 