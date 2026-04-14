def build_prompt(data):
    description = data["description"]
    industry = data["industry"]
    categories = ", ".join(data["chart_of_accounts"])

    history = ""
    for txn in data["historical_transactions"]:
        history += f"{txn['description']} → {txn['category']}\n"
    prompt = f"""
    You are an AI accountant.

    Transaction: {description}
    Industry: {industry}
    Categories: {categories}

    Past Examples:
    {history}

    IMPORTANT:
    - Return ONLY valid JSON
    - Do NOT include any explanation
    - Do NOT include text before or after JSON

    Format:
    {{
    "category": "string",
    "confidence": number,
    "reason": "string"
    }}
    """
    return prompt