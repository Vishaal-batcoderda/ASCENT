from app.graph.graph_builder import build_graph

graph = build_graph(["risk"])

result = graph.invoke(
    {
        "query": "Analyze Apple",
        "ticker": "AAPL",
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
        "analysis": None,
        "risk": None
    }
)

print(result["risk"])