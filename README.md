# 🏦 Banking Agent with Gemini Integration

This is a console-based **Banking Agent** built using the **OpenAI Agents SDK** with **Google Gemini API** integration.  
It authenticates users via PIN, validates if queries are bank-related using **input guardrails**, and provides account balance information securely.

---

## 🚀 Features

- **PIN Authentication** — Ensures only verified users can access sensitive banking data.
- **Input Guardrails** — Uses a dedicated guardrail agent to detect whether a query is banking-related.
- **Context Passing** — Stores and reuses authenticated user details (name + PIN) across multiple requests.
- **Function Tool Enablement** — The balance-checking function is only enabled when the user is authenticated.
- **Google Gemini API** — Configured via `connection.py` for AI-powered query handling.
- **Async Execution** — Uses `asyncio` to handle event loops for smooth execution.
  
---

## ⚙️ How It Works

1. **User Authentication**  
   - The program first asks for your PIN.
   - Only the correct PIN (`234` in this example) grants access.

2. **Guardrail Check**  
   - The `Guardrail Agent` analyzes your query.
   - If the query is not related to banking, the tool will block execution.

3. **Balance Retrieval**  
   - Once authenticated and approved by guardrails, the system runs `check_balance()`.

4. **Context Usage**  
   - Your `name` and `PIN` are stored in `RunContextWrapper` so they can be reused in subsequent queries.

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Zaibunis/Bank-Agent-Assignment.git
```

### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key
Create a .env file in the root directory.

Add the following line:

```bash
GEMINI_API_KEY=your_real_api_key_here
```

⚠️ Do not hardcode your API key into connection.py. Always use .env for security.

---

### ▶️ Usage
Run the banking agent:

```bash
uv run bank_agent.py
```
# Example session

```bash
What is your PIN? 234
The balance of the account is $100000
```

---

### 🛠 Dependencies

1.OpenAI Agents SDK

2.Google Gemini API

3.pydantic — Data validation

4.asyncio — Asynchronous execution

---

# Made with ❤ by [Faria Mustaqim](https://github.com/Zaibunis)
