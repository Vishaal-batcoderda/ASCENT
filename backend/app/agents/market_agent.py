from app.services.market_service import market_service


class MarketAgent:

    def analyze(self, ticker: str):

        stock = market_service.get_stock_info(ticker)
        history = market_service.get_historical_data(ticker)

        return {
            "stock": stock,
            "history": history
        }


market_agent = MarketAgent()