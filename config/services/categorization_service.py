from services.context_builder import build_prompt
from services.llm_service import LLMService
from utils.parser import parse_response

class CategorizationService:

    def __init__(self):
        self.llm = LLMService()

    def categorize(self, data):
        prompt = build_prompt(data)
        raw_response = self.llm.get_response(prompt)
        parsed = parse_response(raw_response)
        return parsed


def adjust_confidence(result, data):
    confidence = result.get("confidence", 0.5)

    # vendor match boost
    if "swiggy" in data["description"].lower():
        confidence += 0.05

    # limit max
    return min(confidence, 0.99)