from fastapi import APIRouter
from app.services.market_service import market_service

router = APIRouter(
    prefix="/stock",
    tags=["Stock"]
)


@router.get("/{ticker}")
def get_stock(ticker: str):
    return market_service.get_stock_info(ticker)