from app.services.technical_service import technical_service


class TechnicalAgent:

    def analyze(
    self,
    history,
    sma_window: int = 20,
    ema_window: int = 20,
    rsi_window: int = 14,
    macd_fast: int = 12,
    macd_slow: int = 26,
    bollinger_window: int = 20
    ):

        sma = technical_service.calculate_sma(history,sma_window)
        ema = technical_service.calculate_ema(history,ema_window)
        rsi = technical_service.calculate_rsi(history,rsi_window)
        macd = technical_service.calculate_macd(history,macd_fast,macd_slow)

        return {
            "sma": sma.dropna().iloc[-1],
            "ema": ema.dropna().iloc[-1],
            "rsi": rsi.dropna().iloc[-1],
            "macd": macd.dropna().iloc[-1]
        }


technical_agent = TechnicalAgent()