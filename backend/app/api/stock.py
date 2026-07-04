from app.services.market_service import market_service
from app.services.technical_service import technical_service
from fastapi import APIRouter, Query
from app.schemas.responses import (
    StockInfoResponse,
    IndicatorPoint,
    BollingerBandsResponse
)
from app.schemas.requests import AnalysisRequest
from app.orchestrator import orchestrator

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
def get_macd(
    ticker: str,
    fast_window: int = Query(default=12),
    slow_window: int = Query(default=26),
    period: str = Query(default="6mo")
):

    history = market_service.get_historical_data(ticker, period)

    macd = technical_service.calculate_macd(
        history,
        fast_window,
        slow_window
    )

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

@router.post("/analyze")
def analyze_stock(request: AnalysisRequest):

    return orchestrator.run(
        user_query=request.query,
        ticker=request.ticker,
        period=request.period,
        sma_window=request.sma_window,
        ema_window=request.ema_window,
        rsi_window=request.rsi_window,
        macd_fast=request.macd_fast,
        macd_slow=request.macd_slow,
        bollinger_window=request.bollinger_window
    )