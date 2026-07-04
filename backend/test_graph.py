from app.graph.ascent_graph import graph

result = graph.invoke(
    {
        "query": "Analyze Take two interactive completely.",
        "ticker": "TTWO",
        "period": "6mo",
        "sma_window": 20,
        "ema_window": 20,
        "rsi_window": 14,
        "macd_fast": 12,
        "macd_slow": 26,
        "bollinger_window": 20,
        "market": None,
        "technical": None,
        "news": None,
        "report": None
    }
)

print(result["report"])