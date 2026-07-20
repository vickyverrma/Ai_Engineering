# Day 1 – First LLM CALL (Python)

## 📌 What I Learned

* Setting up the Groq Python SDK.
* Loading API keys securely using `.env`.
* Sending prompts to an LLM.
* Reading the AI-generated response.

## 📚 Libraries Used

```python
import os
from dotenv import load_dotenv
from groq import Groq
```

## 🔑 Important Syntax

```python
load_dotenv()                         # Load .env variables
os.getenv("GROQ_API_KEY")             # Read API key
client = Groq(api_key=my_api_key)     # Create Groq client

messages = [
    {"role": "user", "content": "Capital of India"}
]

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages
)

print(response.choices[0].message.content)
```

## 📝 Key Points

* Store API keys in a `.env` file.
* Never hardcode secret keys.
* `messages` must be a **list of dictionaries**.
* Each message contains `role` and `content`.
* `chat.completions.create()` sends the request.
* `response.choices[0].message.content` returns the model's reply.

## 🚀 Output

```
The capital of India is New Delhi.
```

### ✅ Day 1 Summary

Successfully connected to the Groq API, sent my first prompt, and received an AI-generated response using the Python SDK.
