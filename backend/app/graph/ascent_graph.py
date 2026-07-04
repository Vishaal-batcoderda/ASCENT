from typing import TypedDict
from langgraph.graph import StateGraph, END
from app.agents.planner_agent import planner_agent
from app.agents.market_agent import market_agent
from app.agents.technical_agent import technical_agent
from app.agents.news_agent import news_agent
from app.agents.report_agent import report_agent

class GraphState(TypedDict):

    query: str

    ticker: str

    period: str

    sma_window: int

    ema_window: int

    rsi_window: int

    macd_fast: int

    macd_slow: int

    bollinger_window: int

    market: dict | None

    technical: dict | None

    news: str | None

    report: str | None
    
    plan: list[str]

def planner_node(state: GraphState):

    plan = planner_agent.create_plan(
        state["query"]
    )

    state["plan"] = plan["agents"]

    return state

def market_node(state: GraphState):

    market = market_agent.analyze(
        ticker=state["ticker"],
        period=state["period"]
    )

    state["market"] = market

    return state

def technical_node(state: GraphState):

    technical = technical_agent.analyze(
        history=state["market"]["history"],
        sma_window=state["sma_window"],
        ema_window=state["ema_window"],
        rsi_window=state["rsi_window"],
        macd_fast=state["macd_fast"],
        macd_slow=state["macd_slow"],
        bollinger_window=state["bollinger_window"]
    )

    state["technical"] = technical

    return state

def news_node(state: GraphState):

    news = news_agent.summarize_news(
        state["ticker"]
    )

    state["news"] = news

    return state

def report_node(state: GraphState):

    report = report_agent.generate_report(

        state["market"]["stock"],

        state["technical"],

        state["news"]

    )

    state["report"] = report

    return state

builder = StateGraph(GraphState)

builder.add_node("planner", planner_node)
builder.add_node("market", market_node)
builder.add_node("technical", technical_node)
builder.add_node("news", news_node)
builder.add_node("report", report_node)

builder.set_entry_point("planner")

builder.add_edge("planner", "market")
builder.add_edge("market", "technical")
builder.add_edge("technical", "news")
builder.add_edge("news", "report")
builder.add_edge("report", END)
graph = builder.compile()