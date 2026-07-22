import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api Not Found")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"
role = "user"
# several prompt at a single time
message_system = {
    "role": "system",
    "content": "A great storyteller and novelist"
}

prompt1 ="Greetings less than 10 words"
prompt2 ="explain global warming in details in less than 40 words"
prompt3 ="why we should practice sprituality in 200 words"
prompts = [prompt1,prompt2,prompt3]
for prompt in prompts:
    message={
    "role" : role,
    "content" : prompt
    }
    messages = [message_system, message]
    response = client.chat.completions.create(model=model,messages=messages)
    usage = response.usage
    print(f" prompt:{prompt} --> your tokens : {usage.prompt_tokens} completion_tokens : {usage.completion_tokens} total tokens : {usage.total_tokens}" )
    print(response.choices[0].message.content)
    # print(f"\nPrompt: {prompt}")
    # print("-" * 40)
    # print(response.choices[0].message.content)
    




