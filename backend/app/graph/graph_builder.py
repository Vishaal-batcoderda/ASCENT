from typing import TypedDict
from langgraph.graph import StateGraph, END

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


AGENT_NODES = {
    "market": market_node,
    "technical": technical_node,
    "news": news_node,
    "report": report_node,
}

DEPENDENCIES = {
    "market": [],
    "technical": ["market"],
    "news": [],
    "report": ["market", "technical", "news"],
}

def resolve_plan(plan: list[str]) -> list[str]:

    resolved = []

    def add_agent(agent: str):

        if agent in resolved:
            return

        for dependency in DEPENDENCIES[agent]:
            add_agent(dependency)

        resolved.append(agent)

    # First resolve all dependent agents
    for agent in plan:
        add_agent(agent)

    return resolved

def build_graph(plan: list[str]):

    plan = resolve_plan(plan)

    if not plan:
        raise ValueError("Execution plan cannot be empty.")

    builder = StateGraph(GraphState)

    for agent in plan:

        if agent not in AGENT_NODES:
            raise ValueError(
                f"Unknown agent in execution plan: {agent}"
            )

        builder.add_node(
            agent,
            AGENT_NODES[agent]
        )

    for i in range(len(plan) - 1):
        builder.add_edge(
            plan[i],
            plan[i + 1]
        )

    builder.set_entry_point(plan[0])

    builder.add_edge(
        plan[-1],
        END
    )

    return builder.compile()