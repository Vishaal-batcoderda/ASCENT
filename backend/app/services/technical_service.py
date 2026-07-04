from fastapi import HTTPException
import pandas as pd


class TechnicalService:
    def _validate_window(self, history: pd.DataFrame, window: int):
        if len(history) < window:
            raise HTTPException(
                status_code=400,
                detail=f"Window size ({window}) cannot be greater than available historical data ({len(history)} trading days)."
            )
    def format_indicator(self, indicator: pd.Series):
        indicator = indicator.dropna()
        return [
            {
                "date": str(date.date()),
                "value": round(float(value), 2)
            }
            for date, value in indicator.items()
        ]    
    
    def calculate_sma(self, history: pd.DataFrame, window: int = 20):
        self._validate_window(history, window)
        sma = history["Close"].rolling(window=window).mean()
        return sma
    
    def calculate_ema(self, history: pd.DataFrame, window: int = 20):
        self._validate_window(history, window)

        ema = history["Close"].ewm(
            span=window,
            adjust=False,
            min_periods=window
        ).mean()

        return ema
    
    def calculate_rsi(self, history: pd.DataFrame, window: int = 14):
        self._validate_window(history, window)

        delta = history["Close"].diff()

        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(window=window).mean()
        avg_loss = loss.rolling(window=window).mean()

        rs = avg_gain / avg_loss

        rsi = 100 - (100 / (1 + rs))

        return rsi
    
    def calculate_macd(
    self,
    history: pd.DataFrame,
    fast_window: int = 12,
    slow_window: int = 26
    ):

        self._validate_window(history, slow_window)
        fast_ema = self.calculate_ema(history, fast_window)
        slow_ema = self.calculate_ema(history, slow_window)

        macd = fast_ema - slow_ema

        return macd

    def calculate_bollinger_bands(self,history: pd.DataFrame,window: int = 20):

        self._validate_window(history, window)

        sma = self.calculate_sma(history, window)

        std = history["Close"].rolling(window=window).std()

        upper_band = sma + (2 * std)

        lower_band = sma - (2 * std)

        return {
            "upper": upper_band,
            "middle": sma,
            "lower": lower_band
        }
    
technical_service = TechnicalService()