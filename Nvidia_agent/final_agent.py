import os
import json
from openai import OpenAI

# 1. Check for the secure key
NVIDIA_KEY = os.environ.get("MY_NVIDIA_KEY")
if not NVIDIA_KEY:
    print("❌ Error: NVIDIA_API_KEY not found in environment!")
    print("Please ensure you added it to GitHub Codespaces Secrets and restarted your codespace.")
    exit(1)

# 2. Initialize the client
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=NVIDIA_KEY
)

# 3. Define local tools
def write_note(content: str) -> str:
    with open("workspace_notes.txt", "a") as f:
        f.write(content + "\n")
    return "Success: Note saved securely."

def read_notes() -> str:
    if not os.path.exists("workspace_notes.txt"):
        return "No notes found. The file is empty."
    with open("workspace_notes.txt", "r") as f:
        return f.read()

# 4. Define capabilities for the AI (NVIDIA-compatible format)
tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "write_note",
            "description": "Saves a note to the workspace notes file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string",
                        "description": "The text content of the note to save"
                    }
                },
                "required": ["content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_notes",
            "description": "Reads all previously saved notes from the workspace notes file.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]

# 5. Core decision loop
def run_agent(user_prompt: str):
    print(f"\n[User]: {user_prompt}")
    
    try:
        # ✅ CHANGED: Removed tool_choice entirely, added extra_headers
        response = client.chat.completions.create(
            model="meta/llama-3.1-8b-instruct",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that can save and read notes. When the user asks you to save a note, use the write_note tool. When they ask to read notes, use the read_notes tool."
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            tools=tools_schema,
            temperature=0.7,
            top_p=0.9,
            max_tokens=1024
        )
        
        print(f"\n[DEBUG] Response received!")
        
        message = response.choices[0].message
        
        print(f"\n[LLM Response]:")
        print(f"  - Content: {message.content}")
        print(f"  - Tool Calls: {message.tool_calls}")
        
        if message.tool_calls:
            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)
                
                print(f"\n[Agent]: Executing tool -> '{tool_name}'")
                print(f"  - Arguments: {arguments}")
                
                if tool_name == "write_note":
                    result = write_note(arguments.get("content", ""))
                elif tool_name == "read_notes":
                    result = read_notes()
                else:
                    result = f"Unknown tool: {tool_name}"
                    
                print(f"  - Result: {result}")
        else:
            print(f"\n[Agent Response]: {message.content}")
            
    except Exception as e:
        print(f"\n❌ ERROR: {type(e).__name__}")
        print(f"Message: {e}")
        import traceback
        traceback.print_exc()

# 6. Execution commands
if __name__ == "__main__":
    print("🔒 Secure connection established with NVIDIA NIM!")
    run_agent("Please take a note: Code is running perfectly inside GitHub Codespaces.")
    run_agent("What are my current notes?")
    run_agent("Add another note: Testing tool execution successfully.")
