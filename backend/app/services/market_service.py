import yfinance as yf
from fastapi import HTTPException

class MarketService:
    def _validate_stock(self, info: dict, ticker: str):
        if not info or info.get("currentPrice") is None:
            raise HTTPException(
                status_code=404,
                detail=f"Ticker '{ticker.upper()}' not found."
            )
        
    def get_stock_info(self, ticker: str):
        stock = yf.Ticker(ticker)
        info = stock.info
        self._validate_stock(info, ticker)
        
        return {
            "ticker": ticker.upper(),
            "company": info.get("longName"),
            "current_price": info.get("currentPrice"),
            "market_cap": info.get("marketCap"),
            "volume": info.get("volume"),
            "high_52_week": info.get("fiftyTwoWeekHigh"),
            "low_52_week": info.get("fiftyTwoWeekLow")
        }
    
    def get_historical_data(self, ticker: str, period: str = "6mo"):
        stock = yf.Ticker(ticker)

        history = stock.history(period=period)

        if history.empty:
            raise HTTPException(
                status_code=404,
                detail=f"No historical data found for '{ticker.upper()}'."
            )

        return history[
            ["Open", "High", "Low", "Close", "Volume"]
        ]

market_service = MarketService()