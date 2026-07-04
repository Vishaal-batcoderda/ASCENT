from app.services.technical_service import technical_service


class TechnicalAgent:

    def analyze(self, history):

        sma = technical_service.calculate_sma(history)
        ema = technical_service.calculate_ema(history)
        rsi = technical_service.calculate_rsi(history)
        macd = technical_service.calculate_macd(history)

        return {
            "sma": sma.dropna().iloc[-1],
            "ema": ema.dropna().iloc[-1],
            "rsi": rsi.dropna().iloc[-1],
            "macd": macd.dropna().iloc[-1]
        }


technical_agent = TechnicalAgent()