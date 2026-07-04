from pydantic import BaseModel


class IndicatorPoint(BaseModel):
    date: str
    value: float
    
class StockInfoResponse(BaseModel):
    ticker: str
    company: str | None
    current_price: float | None
    market_cap: int | None
    volume: int | None
    high_52_week: float | None
    low_52_week: float | None

class BollingerBandsResponse(BaseModel):
    upper: list[IndicatorPoint]
    middle: list[IndicatorPoint]
    lower: list[IndicatorPoint]

class TechnicalAnalysisResponse(BaseModel):
    sma: float
    ema: float
    rsi: float
    macd: float
    
class AnalysisResponse(BaseModel):
    market: StockInfoResponse | None = None
    technical: TechnicalAnalysisResponse | None = None
    news: str | None = None
    report: str | None = None