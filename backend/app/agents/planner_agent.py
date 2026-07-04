import json

from app.services.llm_service import llm_service
from app.prompts.planner_prompt import PLANNER_SYSTEM_PROMPT


class PlannerAgent:

    def create_plan(self, user_query: str):

        response = llm_service.chat(
            user_query,
            PLANNER_SYSTEM_PROMPT
        )

        return json.loads(response)


planner_agent = PlannerAgent()