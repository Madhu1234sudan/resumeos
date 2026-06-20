from services.llm_service import (
    LLMService
)

response = LLMService.rewrite_resume(
    "Hello AI"
)

print(response)