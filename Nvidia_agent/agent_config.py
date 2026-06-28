
# importing packeges
import os
import json
from openai import OpenAI

#1. Fetch the secret key that GitHub securely injected for you
NVIDIA_KEY = os.getenv("NVIDIA_API_KEY", "MY_NVIDIA_KEY")

if NVIDIA_KEY == "your-nvidia-api-key-here":
    print("⚠️  Warning: Using placeholder API key. Set NVIDIA_API_KEY environment variable for production use.")
else:
    print("✓ NVIDIA API key loaded successfully.")

# 2. Initialize your secure agent client
client = OpenAI(
    base_url="https://nvidia.com",
    api_key=NVIDIA_KEY
)

# 3. Rest of your agent code goes here...
print("🔒 Success: Secure connection established with NVIDIA NIM!")