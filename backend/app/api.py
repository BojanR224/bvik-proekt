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



# Testiranje kod

# class NFT(BaseModel):
#     name: str
#     description: str 
#     link: str


# @app.get("/", tags=["root"])
# async def root() -> dict:
#     nft = NFT(name="Dalmation", description="White dog with black dots", link="https://www.purina-arabia.com/sites/default/files/styles/ttt_image_510/public/2021-02/BREED%20Hero%20Mobile_0127_dalmatian_0.jpg?itok=fLkVjLXs&fbclid=IwAR0z7M6c7CN_RRff2q8zyX8cR4BugfYBkT1ypm45x4rUgPGx-eKGp8e9o4g")
#     nft = nft.json()
#     nft = json.loads(nft)
#     nft = {5: nft}
#     aggregate_message = create_aggregate(account, key='test_channel_1', content=nft, address='0xeB1ebA7a4fa4F05e369035c7f97C0f046F550C28')
#     return None



@app.get("/{contract}/{id}")
async def get_nft(contract: str, id: str) -> dict:
    nft_json = fetch_aggregate(account.get_address(), key=contract)

    nft_json = json.dumps(nft_json)
    data = json.loads(nft_json)

    if id in data.keys():
        return {id: data[id]}
    return None


@app.put("/{contract}/{id}")
async def put_nft(contract: str, id: str, name: str, description: str, link: str) -> dict:
    nft_json = fetch_aggregate(account.get_address(), key=contract)

    nft_json = json.dumps(nft_json)
    data = json.loads(nft_json)
    
    print(type(data))

    data[id]["name"] = name
    data[id]["description"] = description
    data[id]["link"] = link

    aggregate_message = create_aggregate(account, key=contract, content=data, address='0xeB1ebA7a4fa4F05e369035c7f97C0f046F550C28')
    return {"Aggregate": aggregate_message}

