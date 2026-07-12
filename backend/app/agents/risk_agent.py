import json

from app.services.llm_service import llm_service
from app.prompts.risk_prompt import RISK_SYSTEM_PROMPT


class RiskAgent:

    def assess_risk(
        self,
        stock: dict,
        technical: dict,
        news_summary: str,
        analysis: str,
    ):

        prompt = f"""
                Stock Information

                Ticker: {stock["ticker"]}
                Company: {stock["company"]}
                Current Price: {stock["current_price"]}

                Technical Indicators

                SMA: {technical["sma"]:.2f}
                EMA: {technical["ema"]:.2f}
                RSI: {technical["rsi"]:.2f}
                MACD: {technical["macd"]:.2f}

                News Summary

                {news_summary}

                Preliminary Analysis

                {analysis}
                """

        response = llm_service.chat(
            prompt,
            RISK_SYSTEM_PROMPT,
        )

        try:
            return json.loads(response)
        
        except json.JSONDecodeError:
            return {
                "level": "Unknown",
                "confidence": 0,
                "dimensions": {
                    "technical": "Unknown",
                    "market": "Unknown",
                    "news": "Unknown",
                    "analysis": "Unknown",
                },
                "summary": "The risk assessment could not be generated.",
                "factors": [],
            }


risk_agent = RiskAgent()