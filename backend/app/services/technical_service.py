from fastapi import HTTPException
import pandas as pd


class TechnicalService:

    def calculate_sma(self, history: pd.DataFrame, window: int = 20):
        if len(history) < window:
            raise HTTPException(
                status_code=400,
                detail=f"Window size ({window}) cannot be greater than available historical data ({len(history)} trading days)."
            )
        sma = history["Close"].rolling(window=window).mean()
        return sma


technical_service = TechnicalService()