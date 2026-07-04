from app.agents.planner_agent import planner_agent
from app.agents.news_agent import news_agent
from app.agents.report_agent import report_agent
from app.agents.market_agent import market_agent
from app.agents.technical_agent import technical_agent


class ASCENTOrchestrator:

    def run(
    self,
    user_query: str,
    ticker: str,
    period: str = "6mo",
    sma_window: int = 20,
    ema_window: int = 20,
    rsi_window: int = 14,
    macd_fast: int = 12,
    macd_slow: int = 26,
    bollinger_window: int = 20
    ):

        plan = planner_agent.create_plan(user_query)

        results = {}

        market = None
        technical = None
        news = None

        for agent in plan["agents"]:

            if agent == "market":

                market = market_agent.analyze(
                                                ticker,
                                                period
                                            )

                results["market"] = market["stock"]


            elif agent == "technical":

                if market is None:
                    market = market_agent.analyze(
                                                    ticker,
                                                    period
                                                )

                technical = technical_agent.analyze(
                                                        history=market["history"],
                                                        sma_window=sma_window,
                                                        ema_window=ema_window,
                                                        rsi_window=rsi_window,
                                                        macd_fast=macd_fast,
                                                        macd_slow=macd_slow,
                                                        bollinger_window=bollinger_window
                                                    )

                results["technical"] = technical


            elif agent == "news":

                news = news_agent.summarize_news(ticker)

                results["news"] = news


            elif agent == "report":

                if market is None:
                    market = market_agent.analyze(
                                                    ticker,
                                                    period
                                                )

                if technical is None:
                    technical = technical_agent.analyze(
                                                            history=market["history"],
                                                            sma_window=sma_window,
                                                            ema_window=ema_window,
                                                            rsi_window=rsi_window,
                                                            macd_fast=macd_fast,
                                                            macd_slow=macd_slow,
                                                            bollinger_window=bollinger_window
                                                        )

                if news is None:
                    news = news_agent.summarize_news(ticker)

                report = report_agent.generate_report(
                    market["stock"],
                    technical,
                    news
                )

                results["report"] = report

        return results

orchestrator = ASCENTOrchestrator()