from app.services.news_service import news_service

articles = news_service.get_news("AAPL")

for article in articles:

    print(article)
    print("-" * 50)