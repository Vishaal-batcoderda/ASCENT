from app.services.llm_service import llm_service

response = llm_service.chat(
    "Explain in one sentence why EMA reacts faster than SMA."
)

print(response)