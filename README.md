# 🚀 Transaction Categorization API

## 📌 Overview

This is a backend-only Django REST API that categorizes transactions using an LLM.

Given a transaction, the API returns:

* Category
* Confidence score
* Reason

---

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd transaction_ai
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django djangorestframework openai python-dotenv
```

### 4. Run server

```bash
python manage.py runserver
```

---

## 🔑 How to Configure API Key

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

Make sure:

* No quotes around the key
* No extra spaces
* Restart server after adding

---

## 📡 API Endpoints

### 🔹 POST /api/categorize/

---

### 📥 Request JSON

```json
{
  "description": "Paid ₹500 to Swiggy",
  "vendor": "Swiggy",
  "company_id": "123",
  "industry": "Food",
  "chart_of_accounts": ["Food", "Travel", "Office"],
  "historical_transactions": [
    {"description": "Zomato order", "category": "Food"}
  ]
}
```

---

### 📤 Response JSON

```json
{
  "category": "Food",
  "confidence": 0.95,
  "reason": "Food delivery service"
}
```

---

## 📦 JSON Schema (Deterministic Output)

```json
{
  "category": "string",
  "confidence": "float (0 to 1)",
  "reason": "string"
}
```

---
