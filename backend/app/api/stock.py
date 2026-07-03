from fastapi import APIRouter
from app.services.market_service import market_service
from fastapi import APIRouter, Query

router = APIRouter(
    prefix="/stock",
    tags=["Stock"]
)


@router.get("/{ticker}")
def get_stock(ticker: str):
    return market_service.get_stock_info(ticker)

@router.get("/{ticker}/history")
def get_stock_history(ticker: str,period: str = Query(default="6mo")):
    
    history = market_service.get_historical_data(ticker, period)

    return history.reset_index().to_dict(orient="records")