import json
import re

def parse_response(response_text):
    try:
        # JSON extract using regex
        json_match = re.search(r"\{.*\}", response_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())

        return {
            "category": "Unknown",
            "confidence": 0.0,
            "reason": "No JSON found"
        }

    except Exception as e:
        return {
            "category": "Unknown",
            "confidence": 0.0,
            "reason": f"Parsing failed: {str(e)}"
        }