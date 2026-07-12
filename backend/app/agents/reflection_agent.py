import json

from app.services.llm_service import llm_service
from app.prompts.reflection_prompt import REFLECTION_SYSTEM_PROMPT


class ReflectionAgent:

    def review_analysis(
        self,
        stock: dict,
        technical: dict,
        news_summary: str,
        analysis: str,
        risk: dict,
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
                
                Bollinger Bands:

                Upper Band: {technical["bollinger"]["upper"]:.2f}
                Middle Band: {technical["bollinger"]["middle"]:.2f}
                Lower Band: {technical["bollinger"]["lower"]:.2f}

                News Summary

                {news_summary}

                Analysis

                {analysis}

                Risk Assessment

                {json.dumps(risk, indent=2)}
                """

        response = llm_service.chat(
            prompt,
            REFLECTION_SYSTEM_PROMPT,
        )

        try:
            return json.loads(response)

        except json.JSONDecodeError:
            print("ReflectionAgent failed to parse LLM response:")
            print(response)
            
            return {
                "overall_quality": "Unknown",
                "confidence": 0,
                "summary": "Reflection could not be generated.",
                "strengths": [],
                "weaknesses": [],
                "missing_information": [],
                "verdict": ""
            }


reflection_agent = ReflectionAgent()