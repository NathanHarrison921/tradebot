import asyncio
from drift_client import get_drift_client
from logger import log

async def main():
    client = await get_drift_client()

    # List available perpetual markets (coins)
    markets = client.perp_market_map.values()

    print("🪙 Available Markets:\n")
    for market in markets:
        symbol = market.name.decode('utf-8')
        price = client.get_perp_market_price(market.market_index) / 1e6
        funding = client.get_perp_funding_rate(market.market_index)
        print(f"Market: {symbol}, Price: {price:.2f}, Funding Rate: {funding:.4f}")

    await client.unsubscribe()

if __name__ == "__main__":
    asyncio.run(main())
