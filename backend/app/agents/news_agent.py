from app.services.news_service import news_service
from app.services.llm_service import llm_service
from app.prompts.news_prompt import NEWS_SYSTEM_PROMPT


class NewsAgent:

    def summarize_news(self, ticker: str):

        articles = news_service.get_news(ticker)

        prompt = f"Recent news for {ticker}:\n\n"

        for index, article in enumerate(articles, start=1):

            prompt += (
                f"{index}.\n"
                f"Title: {article['title']}\n"
                f"Summary: {article['summary']}\n\n"
            )

        prompt += f"""
                    You are analyzing news for the stock: {ticker}.

                    The articles below may include:
                    - direct company news
                    - competitor news
                    - supplier/customer news
                    - broader market news

                    Your job is NOT to summarize every article.

                    Instead:

                    1. Focus on news that could materially impact {ticker}.
                    2. Ignore articles that are unrelated.
                    3. If another company is mentioned, explain WHY it matters to {ticker}.
                    4. Provide an overall sentiment:
                    - Bullish
                    - Neutral
                    - Bearish
                    5. Keep the summary under 120 words.
                    6. Do not invent information not present in the articles.
                    """

        return llm_service.chat(
            prompt,
            NEWS_SYSTEM_PROMPT
        )

news_agent = NewsAgent()