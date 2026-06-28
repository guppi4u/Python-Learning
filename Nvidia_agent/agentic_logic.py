# Initialize client pointing directly to NVIDIA's servers
client = OpenAI(
    base_url="https://nvidia.com",
    api_key=os.environ.get("NVIDIA_API_KEY")
)

# Tell the LLM what tools it has access to
tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "write_note",
            "description": "Call this to save a brand new note to the text file.",
            "parameters": {
                "type": "object",
                "properties": {"content": {"type": "string", "description": "The exact note text to save"}},
                "required": ["content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_notes",
            "description": "Call this to look up and read all previously recorded notes.",
            "parameters": {"type": "object", "properties": {}}
        }
    }
]

"""
Why this structure matters: The LLM doesn't directly call your Python functions. Instead, 
it outputs structured JSON like {"name": "write_note", "arguments": {"content": "Buy milk"}},
 and your code translates that into an actual function call.

"""
def run_agent(user_prompt: str):
    print(f"\n[User]: {user_prompt}")
    
    # 1. Ask the NVIDIA model what action to take
    response = client.chat.completions.create(
        model="meta/llama-3-70b-instruct", 
        messages=[
            {"role": "system", "content": "You are a helpful office agent. Use your tools to read and write notes when asked."},
            {"role": "user", "content": user_prompt}
        ],
        tools=tools_schema,
        tool_choice="auto"
    )
    
    message = response.choices[0].message
    
    # 2. Check if the model wants to run a tool
    if message.tool_calls:
        for tool_call in message.tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            
            print(f"[Agent]: Planning action -> calling tool '{tool_name}'...")
            
            # Execute the correct function
            if tool_name == "write_note":
                result = write_note(arguments.get("content"))
            elif tool_name == "read_notes":
                result = read_notes()
                
            print(f"[Tool Output]: {result}")
    else:
        # If no tool was needed, it just answers directly
        print(f"[Agent]: {message.content}")

