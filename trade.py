from logger import log

async def show_market_info(drift, symbol="BTC"):
    market = await drift.get_perp_market(symbol)
    price = market.get_price()
    funding = market.get_current_funding_rate()

    log(f"Market: {symbol}")
    log(f"Price: {price}")
    log(f"Funding Rate: {funding}")