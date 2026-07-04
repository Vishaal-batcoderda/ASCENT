from app.agents.planner_agent import planner_agent

plan = planner_agent.create_plan(
    "Analyze Apple stock completely."
)

print(plan)