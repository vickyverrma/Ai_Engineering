# IMPORTING DEPENDENCIES
import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# LOADING .ENV
load_dotenv()

# API KEY
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Api Not Found")

# create client
client = Groq(api_key=my_api_key)

# CHOOSING MODEL
model = "openai/gpt-oss-120b"


role = "user"
prompt = "i am opening a food stall suggest me two or three name for my cart"
# SYSTEM UNDERSSTANDING
message_system={
    "role" : "system",
    "content" : "Senior content writer and story teller"
}

message={
    "role" : role,
    "content" : prompt
}
messages = [message_system, message]

# GENERATE RESPONSE
response = client.chat.completions.create(model=model,messages=messages,temperature=2)
print(response.choices[0].message.content)


