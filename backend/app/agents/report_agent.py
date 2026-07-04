from app.services.market_service import market_service
from app.services.technical_service import technical_service
from app.services.llm_service import llm_service
from app.prompts.report_prompt import REPORT_SYSTEM_PROMPT
from app.agents.news_agent import news_agent

class ReportAgent:

    def generate_report(self,stock: dict,technical: dict,news_summary: str):

        prompt = f"""
                    Analyze this stock using ONLY the information below.

                    Ticker: {stock["ticker"]}
                    Company: {stock["company"]}
                    Current Price: {stock["current_price"]}

                    Technical Indicators:
                    - SMA (20): {technical["sma"]:.2f}
                    - EMA (20): {technical["ema"]:.2f}
                    - RSI (14): {technical["rsi"]:.2f}
                    - MACD: {technical["macd"]:.2f}
                    
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