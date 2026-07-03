from app.services.market_service import market_service
from app.services.technical_service import technical_service
from fastapi import APIRouter, Query
from app.schemas.responses import (
    StockInfoResponse,
    IndicatorPoint,
    BollingerBandsResponse
)

router = APIRouter(
    prefix="/stock",
    tags=["Stock"]
)

@router.get("/{ticker}", response_model=StockInfoResponse)
def get_stock(ticker: str):
    return market_service.get_stock_info(ticker)

@router.get("/{ticker}/history")
def get_stock_history(ticker: str,period: str = Query(default="6mo")):

    history = market_service.get_historical_data(ticker, period)

    return history.reset_index().to_dict(orient="records")

@router.get("/{ticker}/sma", response_model=list[IndicatorPoint])
def get_sma(ticker: str,window: int = Query(default=20),period: str = Query(default="6mo")):

    history = market_service.get_historical_data(ticker,period)

    sma = technical_service.calculate_sma(history,window)

    return technical_service.format_indicator(sma)

@router.get("/{ticker}/ema", response_model=list[IndicatorPoint])
def get_ema(ticker: str,window: int = Query(default=20),period: str = Query(default="6mo")):

    history = market_service.get_historical_data(ticker, period)

    ema = technical_service.calculate_ema(history, window)

    return technical_service.format_indicator(ema)

@router.get("/{ticker}/rsi", response_model=list[IndicatorPoint])
def get_rsi(ticker: str,window: int = Query(default=14),period: str = Query(default="6mo")):

    history = market_service.get_historical_data(ticker, period)

    rsi = technical_service.calculate_rsi(history, window)

    return technical_service.format_indicator(rsi)

@router.get("/{ticker}/macd", response_model=list[IndicatorPoint])
def get_macd(ticker: str,period: str = Query(default="6mo")):
    
    history = market_service.get_historical_data(ticker, period)
    macd = technical_service.calculate_macd(history)

    return technical_service.format_indicator(macd)

@router.get(
    "/{ticker}/bollinger",
    response_model=BollingerBandsResponse
)
def get_bollinger(ticker: str,window: int = Query(default=20),period: str = Query(default="6mo")):

    history = market_service.get_historical_data(ticker, period)

    bands = technical_service.calculate_bollinger_bands(history, window)

    return {
        "upper": technical_service.format_indicator(bands["upper"]),
        "middle": technical_service.format_indicator(bands["middle"]),
        "lower": technical_service.format_indicator(bands["lower"])
    }