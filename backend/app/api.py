import string
from webbrowser import get
from coincurve import PrivateKey
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from aleph_client.synchronous import create_aggregate, get_messages, fetch_aggregate
from aleph_client.chains.ethereum import ETHAccount
import json

app = FastAPI()

private_key = bytes.fromhex("d2c56ff4e0dc6d23185f5fe6d85c96af8512a8fce3cf576f8931e80bb0e6d637")

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
async def read_root(nft) -> dict:
    nft_json = await fetch_aggregate(account.get_address(), key='bvik-proekt')

    #aggregate_message = await create_aggregate(account, key='bvik-proekt', content={'2':2}, address='0xeB1ebA7a4fa4F05e369035c7f97C0f046F550C28')
    return {"message": json.loads(nft_json)}


# @app.get("/v1/{id}")
# async def list_all_messages(id: str):
#     aggregate = await get_messages()
#     return aggregate



# button 
# function
# create_aggreate
# 