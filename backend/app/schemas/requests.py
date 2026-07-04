from pydantic import BaseModel


class AnalysisRequest(BaseModel):

    ticker: str

    query: str

    period: str = "6mo"

    sma_window: int = 20

    ema_window: int = 20

    rsi_window: int = 14

    macd_fast: int = 12

    macd_slow: int = 26

    bollinger_window: int = 20