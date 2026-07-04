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

        prompt += """
                Summarize the overall news sentiment.

                Mention:
                - Key events
                - Overall sentiment (Bullish / Neutral / Bearish)
                - Keep it under 100 words.
                """

        return llm_service.chat(
            prompt,
            NEWS_SYSTEM_PROMPT
        )

news_agent = NewsAgent()