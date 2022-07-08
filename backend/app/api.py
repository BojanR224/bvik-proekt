from webbrowser import get
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from aleph_client.synchronous import create_aggregate, get_messages, fetch_aggregate
from aleph_client.chains.ethereum import ETHAccount
import json
from pydantic import BaseModel

app = FastAPI()

private_key = bytes.fromhex("d2c56ff4e0dc6d23185f5fe6d85c96af8512a8fce3cf576f8931e80bb0e6d637")

account = ETHAccount(private_key)

# origins = [
#     "http://localhost:3000",
#     "localhost:3000"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

class NFT(BaseModel):
    name: str
    description: str 
    link: str


@app.get("/", tags=["root"])
async def root() -> dict:
    nft = NFT(name="Dalmation", description="White dog with black dots", link="https://www.purina-arabia.com/sites/default/files/styles/ttt_image_510/public/2021-02/BREED%20Hero%20Mobile_0127_dalmatian_0.jpg?itok=fLkVjLXs&fbclid=IwAR0z7M6c7CN_RRff2q8zyX8cR4BugfYBkT1ypm45x4rUgPGx-eKGp8e9o4g")
    nft = nft.json()
    aggregate_message = create_aggregate(account, key='key', content=nft, address='0xeB1ebA7a4fa4F05e369035c7f97C0f046F550C28')
    return None

# contract e klucot
# id e adresata na nft

@app.get("/{key}")
async def get_nft(contract: str, id: str) -> dict:
    nft_json = fetch_aggregate(account.get_address(), key=contract)
    nft_json = json.dumps(nft_json)
    
    return nft_json[id]

# put : dodavame nft vo kolekcijata, prva treba da se proveri dali go ima vo kolekicata; ako go ima se menja se "pravi neso"; ako go nema go cel nft vo kolekcija

@app.get("/{contract}/{id}")
async def put_nft(contract: str, id: str, json: str) -> dict:
    nft_json = fetch_aggregate(account.get_address(), key=contract)
    nft_json = json.dumps(nft_json)

    #aggregate_message = create_aggregate(account, key='key', content={'id': 23}, address='0xeB1ebA7a4fa4F05e369035c7f97C0f046F550C28')
    #json_message = json.dumps(aggregate_message)
    #print(json_message['item_content']['content']['id'])

    return nft_json


# vo urlto network/id