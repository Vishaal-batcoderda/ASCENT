from backend.app.agents.analysis_agent import report_agent

report = report_agent.generate_report("AAPL")

print(report)