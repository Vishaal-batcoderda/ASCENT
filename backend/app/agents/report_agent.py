from app.services.market_service import market_service
from app.services.technical_service import technical_service
from app.services.llm_service import llm_service
from app.prompts.report_prompt import REPORT_SYSTEM_PROMPT
from app.agents.news_agent import news_agent

class ReportAgent:

    def generate_report(self, ticker: str):

        # Step 1
        stock = market_service.get_stock_info(ticker)

        # Step 2
        history = market_service.get_historical_data(ticker)

        # Step 3
        sma = technical_service.calculate_sma(history)
        ema = technical_service.calculate_ema(history)
        rsi = technical_service.calculate_rsi(history)
        macd = technical_service.calculate_macd(history)
        latest_sma = sma.dropna().iloc[-1]
        latest_ema = ema.dropna().iloc[-1]
        latest_rsi = rsi.dropna().iloc[-1]
        latest_macd = macd.dropna().iloc[-1]
        news_summary = news_agent.summarize_news(ticker)

        prompt = f"""
                    Analyze this stock using ONLY the information below.

                    Ticker: {stock["ticker"]}
                    Company: {stock["company"]}
                    Current Price: {stock["current_price"]}

                    Technical Indicators:
                    - SMA (20): {latest_sma:.2f}
                    - EMA (20): {latest_ema:.2f}
                    - RSI (14): {latest_rsi:.2f}
                    - MACD: {latest_macd:.2f}
                    
                    Recent News Summary:
                    {news_summary}

                    Return ONLY this Markdown format:

                    ## Market Summary
                    Maximum 2 sentences.

                    ## Technical Analysis
                    Maximum 3 bullet points.

                    ## Overall Opinion
                    Maximum 2 sentences.

                    ## Disclaimer
                    One sentence stating this is not financial advice.

                    Do not add any extra sections.
                    Do not repeat the input values unnecessarily.
                    Do not make assumptions beyond the supplied data.
                    """
        report = llm_service.chat(
                                    prompt,
                                    REPORT_SYSTEM_PROMPT
                                )
        
        return report
    
report_agent = ReportAgent()