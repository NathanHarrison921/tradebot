import asyncio
import json
from solders.keypair import Keypair
from solana.rpc.async_api import AsyncClient
from driftpy.constants.config import configs
from driftpy.drift_client import DriftClient
from anchorpy import Wallet

from config import RPC_URL, WALLET_PATH

async def load_wallet():
    with open(WALLET_PATH, 'r') as f:
        secret = json.load(f)
        return Keypair.from_bytes(bytes(secret))

async def get_drift_client():
    # ✅ this is the correct key for DriftPy
    drift_config = configs["mainnet"]  # don't use "mainnet-beta"
    
    keypair = await load_wallet()
    conn = AsyncClient(RPC_URL)
    wallet = Wallet(keypair)
    
    # ✅ create the client with config
    client = DriftClient(conn, wallet, drift_config)
    
    # ✅ subscribe WITHOUT passing config again
    await client.subscribe()  # ❌ don't do: client.subscribe(drift_config)
    
    return client