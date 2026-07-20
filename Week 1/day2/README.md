# Day 2 – System Role & Temperature

## 📌 What I Learned

* Using the **system role** to define the AI's behavior.
* Sending multiple messages in a conversation.
* Controlling response creativity with the `temperature` parameter.
* Building a structured chat request using the Groq SDK.

## 📚 Libraries Used

```python
import os
from dotenv import load_dotenv
from groq import Groq
```

## 🔑 Important Syntax

```python
message_system = {
    "role": "system",
    "content": "Senior content writer and story teller"
}

message = {
    "role": "user",
    "content": "I am opening a food stall. Suggest 3 names."
}

messages = [message_system, message]

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    temperature=2
)

print(response.choices[0].message.content)
```

## 📝 Key Points

* The **system** role tells the model how it should behave.
* The **user** role contains the actual prompt.
* `messages` is a list that preserves the conversation.
* `temperature` controls the randomness of the response.
* Lower temperature (`0–0.5`) gives focused and consistent answers.
* Higher temperature (`1–2`) produces more creative and diverse outputs.
* Access the generated text using `response.choices[0].message.content`.

## 🚀 Example Output

```
1. Spice Street
2. The Tasty Cart
3. Flavor Junction
```

### ✅ Day 2 Summary

Learned how to use the **system role** to guide the AI's personality and the **temperature** parameter to control the creativity of its responses while generating chat completions with the Groq API.