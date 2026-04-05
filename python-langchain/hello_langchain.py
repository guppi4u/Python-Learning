import os
from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage

def main():
    # os.getenv() looks for the secret GitHub injected
    key = os.getenv("LANGCHAIN_KEY")

    if not key:
        print("❌ Error: API Key not found in environment variables.")
        return

    # Pass the key explicitly to avoid any "guessing" by the library
    model = ChatAnthropic(
        model="claude-sonnet-4-6",
        api_key=key, 
        temperature=0
    )

    print("--- 🤖 Testing Claude 4.6 Connection ---")
    try:
        response = model.invoke([HumanMessage(content="Hello Claude!")])
        print(f"Success: {response.content}")
    except Exception as e:
        print(f"Connection Failed: {e}")

if __name__ == "__main__":
    main()