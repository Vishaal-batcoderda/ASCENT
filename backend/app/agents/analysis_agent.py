from app.services.llm_service import llm_service
from app.prompts.analysis_prompt import ANALYSIS_SYSTEM_PROMPT

class AnalysisAgent:

    def generate_analysis(self,stock: dict,technical: dict,news_summary: str):

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

                    Bollinger Bands:
                    - Upper Band: {technical["bollinger"]["upper"]:.2f}
                    - Middle Band: {technical["bollinger"]["middle"]:.2f}
                    - Lower Band: {technical["bollinger"]["lower"]:.2f}
                    
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
        analysis = llm_service.chat(
                                    prompt,
                                    ANALYSIS_SYSTEM_PROMPT
                                )
        
        return analysis
    
analysis_agent = AnalysisAgent()