
import asyncio
from drift_client import get_drift_client

async def show_open_positions():
    client = await get_drift_client()
    user = client.get_user()

    print("📊 Open Positions:\n")
    for position in user.get_open_perp_positions():
        if position.base_asset_amount == 0:
            continue

        market_index = position.market_index
        market = client.get_perp_market_account(market_index)
        symbol = market.name.decode()

        entry_price = user.get_entry_price(market_index) / 1e6
        current_price = client.get_perp_market_price(market_index) / 1e6
        pnl = user.get_unrealized_pnl(True, market_index) / 1e6
        size = position.base_asset_amount / 1e9  # Drift uses 1e9 precision for size
        side = "LONG" if size > 0 else "SHORT"

        print(f"{symbol} | {side:<5} | Entry: ${entry_price:.2f} | Price: ${current_price:.2f} | PnL: ${pnl:.2f} | Size: {abs(size):.4f}")

    await client.unsubscribe()

if __name__ == "__main__":
    asyncio.run(show_open_positions())