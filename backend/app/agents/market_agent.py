from app.services.market_service import market_service


class MarketAgent:

    def analyze(
    self,
    ticker: str,
    period: str = "6mo"
    ):

        stock = market_service.get_stock_info(ticker)
        history = market_service.get_historical_data(ticker,period)

        return {
            "stock": stock,
            "history": history
        }


market_agent = MarketAgent()