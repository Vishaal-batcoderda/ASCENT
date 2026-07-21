from app.services.llm_service import llm_service
from app.prompts.report_prompt import REPORT_SYSTEM_PROMPT


class ReportAgent:

    def generate_report(
        self,
        stock: dict,
        technical: dict,
        news_summary: str,
        analysis: str,
        risk: dict,
        reflection: dict,
    ):

        prompt = f"""
                You are given the outputs produced by previous specialized AI agents.

                Stock Information

                Ticker: {stock["ticker"]}
                Company: {stock["company"]}
                Current Price: {stock["current_price"]}

                Technical Indicators

                SMA: {technical["sma"]:.2f}
                EMA: {technical["ema"]:.2f}
                RSI: {technical["rsi"]:.2f}
                MACD: {technical["macd"]:.2f}

                Bollinger Bands

                Upper Band: {technical["bollinger"]["upper"]:.2f}
                Middle Band: {technical["bollinger"]["middle"]:.2f}
                Lower Band: {technical["bollinger"]["lower"]:.2f}
                
                News Summary

                {news_summary}

                Preliminary Analysis

                {analysis}

                Risk Assessment

                Overall Risk Level: {risk["level"]}

                Confidence: {risk["confidence"]}

                Summary:
                {risk["summary"]}

                Risk Factors:
                {chr(10).join(f"- {factor}" for factor in risk["factors"])}

                Reflection

                Overall Quality: {reflection["overall_quality"]}

                Confidence: {reflection["confidence"]}

                Summary:
                {reflection["summary"]}

                Strengths:
                {chr(10).join(f"- {item}" for item in reflection["strengths"])}

                Weaknesses:
                {chr(10).join(f"- {item}" for item in reflection["weaknesses"])}

                Missing Information:
                {chr(10).join(f"- {item}" for item in reflection["missing_information"])}

                Verdict:
                {reflection["verdict"]}

                Generate a clear, professional investment report using ONLY the information above.

                Follow EXACTLY this Markdown structure:

                # {stock["company"]} ({stock["ticker"]}) Investment Report

                ## Market Summary

                ## Technical Analysis

                ### SMA and EMA Analysis

                ### RSI and MACD Analysis

                ### Bollinger Bands Analysis

                ## News Summary

                ## Preliminary Analysis

                ## Risk Assessment

                ## Reflection

                ## Overall Recommendation

                ## Disclaimer

                Requirements:
                - Use '#' for the report title.
                - Use '##' for major sections.
                - Use '###' for subsections.
                - Leave one blank line after every heading.
                - Use bullet points for strengths, weaknesses, risk factors, and missing information.
                - Do NOT use underlined headings (=== or ---).
                - Return ONLY valid Markdown.
                """

        report = llm_service.chat(
            prompt,
            REPORT_SYSTEM_PROMPT,
        )

        return report


report_agent = ReportAgent()