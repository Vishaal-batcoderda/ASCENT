from app.orchestrator import orchestrator

results = orchestrator.run(
    user_query="What's the news regarding TTWO?",
    ticker="TTWO"
)

for key, value in results.items():
    print(f"\n===== {key.upper()} =====\n")
    print(value)