from app.orchestrator import orchestrator

results = orchestrator.run(
    user_query="Analyze Apple stock completely.",
    ticker="AAPL",
    period="1y",
    sma_window=50,
    ema_window=30,
    rsi_window=21,
    macd_fast=8,
    macd_slow=21,
    bollinger_window=30
)

for key, value in results.items():
    print(f"\n===== {key.upper()} =====\n")
    print(value)