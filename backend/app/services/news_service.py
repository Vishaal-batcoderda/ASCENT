import yfinance as yf


class NewsService:

    def get_news(self, ticker: str, limit: int = 5):

        stock = yf.Ticker(ticker)

        news = stock.news

        articles = []
        count = 0

        for article in news:

            if count >= limit:
                break

            content = article.get("content", {})
            title = content.get("title", "")
            summary = content.get("summary", "")

            text = f"{title} {summary}".lower()

            # if ticker.lower() not in text:
            #     continue

            articles.append(
                            {
                                "title": title,
                                "summary": summary,
                                "publisher": content.get("provider", {}).get("displayName"),
                                "published": content.get("pubDate"),
                                "url": content.get("canonicalUrl", {}).get("url")
                            }
                        )
            count += 1

        return articles


news_service = NewsService()