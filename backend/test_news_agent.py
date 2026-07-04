from app.agents.news_agent import news_agent

summary = news_agent.summarize_news("AAPL")

print(summary)