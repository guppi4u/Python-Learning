import os
import json
from datetime import datetime
from openai import OpenAI

# ============================================================================
# 1. CONFIGURATION & INITIALIZATION
# ============================================================================

NVIDIA_KEY = os.environ.get("MY_NVIDIA_KEY")
if not NVIDIA_KEY:
    print("❌ Error: NVIDIA_API_KEY not found in environment!")
    print("Please ensure you added it to GitHub Codespaces Secrets and restarted your codespace.")
    exit(1)

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=NVIDIA_KEY
)

NOTES_FILE = "workspace_notes.txt"
HISTORY_FILE = "chat_history.json"

# ============================================================================
# 2. CORE TOOL IMPLEMENTATIONS WITH ERROR HANDLING
# ============================================================================

def write_note(content: str) -> str:
    """Save a note with timestamp."""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(NOTES_FILE, "a") as f:
            f.write(f"[{timestamp}] {content}\n")
        return f"✅ Success: Note saved securely at {timestamp}"
    except IOError as e:
        return f"❌ Error writing note: {str(e)}"
    except Exception as e:
        return f"❌ Unexpected error: {str(e)}"

def read_notes() -> str:
    """Read all saved notes."""
    try:
        if not os.path.exists(NOTES_FILE):
            return "📭 No notes found. The file is empty."
        with open(NOTES_FILE, "r") as f:
            content = f.read().strip()
        return content if content else "📭 No notes found."
    except IOError as e:
        return f"❌ Error reading notes: {str(e)}"

def delete_note(line_number: int) -> str:
    """Delete a specific note by line number."""
    try:
        if not os.path.exists(NOTES_FILE):
            return "❌ No notes file to delete from."
        
        with open(NOTES_FILE, "r") as f:
            lines = f.readlines()
        
        if line_number < 1 or line_number > len(lines):
            return f"❌ Invalid line number. Only {len(lines)} notes exist."
        
        deleted_line = lines.pop(line_number - 1)
        
        with open(NOTES_FILE, "w") as f:
            f.writelines(lines)
        
        return f"✅ Deleted note #{line_number}: {deleted_line.strip()}"
    except Exception as e:
        return f"❌ Error deleting note: {str(e)}"

def search_notes(query: str) -> str:
    """Search for notes matching a query."""
    try:
        if not os.path.exists(NOTES_FILE):
            return "📭 No notes to search."
        
        with open(NOTES_FILE, "r") as f:
            lines = f.readlines()
        
        matches = [f"  {i+1}. {line.strip()}" for i, line in enumerate(lines) if query.lower() in line.lower()]
        
        if not matches:
            return f"🔍 No notes found matching '{query}'"
        
        return f"🔍 Found {len(matches)} matching notes:\n" + "\n".join(matches)
    except Exception as e:
        return f"❌ Error searching notes: {str(e)}"

def export_notes(format_type: str = "txt") -> str:
    """Export notes in different formats."""
    try:
        if not os.path.exists(NOTES_FILE):
            return "❌ No notes to export."
        
        with open(NOTES_FILE, "r") as f:
            content = f.read()
        
        if format_type == "txt":
            export_file = "notes_export.txt"
            with open(export_file, "w") as f:
                f.write(content)
            return f"✅ Notes exported to {export_file}"
        elif format_type == "json":
            export_file = "notes_export.json"
            lines = content.strip().split("\n")
            with open(export_file, "w") as f:
                json.dump({"notes": lines}, f, indent=2)
            return f"✅ Notes exported to {export_file}"
        else:
            return f"❌ Unsupported format: {format_type}"
    except Exception as e:
        return f"❌ Error exporting notes: {str(e)}"

# ============================================================================
# 3. CONVERSATION HISTORY MANAGEMENT
# ============================================================================

def load_chat_history() -> list:
    """Load previous conversation history."""
    try:
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
    except Exception as e:
        print(f"⚠️  Warning: Could not load chat history: {str(e)}")
    return []

def save_chat_history(history: list):
    """Persist conversation history to disk."""
    try:
        with open(HISTORY_FILE, "w") as f:
            json.dump(history, f, indent=2)
    except Exception as e:
        print(f"⚠️  Warning: Could not save chat history: {str(e)}")

def add_to_history(role: str, content: str, history: list):
    """Add a message to conversation history."""
    history.append({"role": role, "content": content})

# ============================================================================
# 4. TOOL SCHEMA DEFINITION
# ============================================================================

tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "write_note",
            "description": "Saves a new timestamped note to the workspace notes file.",
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
            "description": "Reads and displays all previously saved notes.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete_note",
            "description": "Deletes a specific note by its line number.",
            "parameters": {
                "type": "object",
                "properties": {
                    "line_number": {
                        "type": "integer",
                        "description": "The line number of the note to delete (starts at 1)"
                    }
                },
                "required": ["line_number"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_notes",
            "description": "Searches for notes containing a specific keyword or phrase.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search term or phrase to look for in notes"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "export_notes",
            "description": "Exports all notes to a file in the specified format.",
            "parameters": {
                "type": "object",
                "properties": {
                    "format_type": {
                        "type": "string",
                        "enum": ["txt", "json"],
                        "description": "The export format: 'txt' or 'json'"
                    }
                },
                "required": ["format_type"]
            }
        }
    }
]

# ============================================================================
# 5. AGENT EXECUTION WITH MULTI-TURN MEMORY
# ============================================================================

def run_agent(user_prompt: str, conversation_history: list = None):
    """
    Run the agent with tool execution, error handling, and conversational response.
    """
    if conversation_history is None:
        conversation_history = load_chat_history()
    
    print(f"\n{'='*70}")
    print(f"[User]: {user_prompt}")
    print(f"{'='*70}")
    
    # Add user message to history
    add_to_history("user", user_prompt, conversation_history)
    
    try:
        # Call the LLM with conversation history
        response = client.chat.completions.create(
            model="meta/llama-3.1-8b-instruct",
            messages=[
                {
                    "role": "system",
                    "content": """You are a helpful AI assistant managing a personal note-taking system. 
You have access to tools to save, read, search, and export notes. 
When the user asks you to perform an action with notes, use the appropriate tool.
Always provide a friendly, conversational response after using a tool.
Be concise and helpful."""
                }
            ] + conversation_history,
            tools=tools_schema,
            temperature=0.7,
            top_p=0.9,
            max_tokens=1024,
            timeout=60
        )
        
        print(f"\n[DEBUG] Response received successfully!")
        
        message = response.choices[0].message
        tool_was_called = False
        
        # Process tool calls if any
        if message.tool_calls:
            tool_was_called = True
            tool_results = []
            
            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)
                
                print(f"\n[Agent]: Executing tool → '{tool_name}'")
                print(f"  Arguments: {arguments}")
                
                # Execute the appropriate tool
                if tool_name == "write_note":
                    result = write_note(arguments.get("content", ""))
                elif tool_name == "read_notes":
                    result = read_notes()
                elif tool_name == "delete_note":
                    result = delete_note(arguments.get("line_number", 0))
                elif tool_name == "search_notes":
                    result = search_notes(arguments.get("query", ""))
                elif tool_name == "export_notes":
                    result = export_notes(arguments.get("format_type", "txt"))
                else:
                    result = f"❌ Unknown tool: {tool_name}"
                
                print(f"  Result: {result}")
                tool_results.append({
                    "tool_name": tool_name,
                    "result": result
                })
            
            # Build a conversational response using the tool results
            tool_summary = "\n".join([f"- {r['tool_name']}: {r['result']}" for r in tool_results])
            
            # Create a follow-up request to the LLM for a natural response
            follow_up_messages = conversation_history + [
                {
                    "role": "assistant",
                    "content": None,
                    "tool_calls": message.tool_calls
                },
                {
                    "role": "user",
                    "content": f"Tool execution results:\n{tool_summary}\n\nPlease provide a friendly summary response."
                }
            ]
            
            follow_up_response = client.chat.completions.create(
                model="meta/llama-3.1-8b-instruct",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful note-taking assistant. Provide friendly, concise summaries of completed actions."
                    }
                ] + follow_up_messages,
                temperature=0.7,
                max_tokens=512,
                timeout=60
            )
            
            assistant_response = follow_up_response.choices[0].message.content
            print(f"\n[Agent Response]: {assistant_response}")
            add_to_history("assistant", assistant_response, conversation_history)
        
        else:
            # No tool was called, just respond naturally
            assistant_response = message.content
            if assistant_response:
                print(f"\n[Agent Response]: {assistant_response}")
                add_to_history("assistant", assistant_response, conversation_history)
        
        # Save updated conversation history
        save_chat_history(conversation_history)
        
        return conversation_history
    
    except Exception as e:
        error_msg = f"❌ ERROR: {type(e).__name__}\nMessage: {str(e)}"
        print(f"\n{error_msg}")
        import traceback
        traceback.print_exc()
        return conversation_history
# ============================================================================
# 6. INTERACTIVE CONVERSATION LOOP
# ============================================================================

def interactive_session():
    """
    Run an interactive conversation session with the agent.
    Type 'quit', 'exit', or 'close' to end the session.
    """
    print("🔒 Secure connection established with NVIDIA NIM!")
    print("📝 Advanced Note-Taking Agent Started")
    print("=" * 70)
    print("Commands:")
    print("  - Type your message to interact with the agent")
    print("  - Type 'quit', 'exit', or 'close' to end the session")
    print("  - Type 'history' to see conversation history")
    print("  - Type 'clear' to clear conversation history")
    print("=" * 70 + "\n")
    
    # Load existing conversation history
    conversation_history = load_chat_history()
    
    if conversation_history:
        print(f"✅ Loaded {len(conversation_history)} messages from previous session\n")
    
    while True:
        try:
            # Get user input
            user_input = input("\n[You]: ").strip()
            
            # Handle special commands
            if not user_input:
                print("⚠️  Please enter a message.")
                continue
            
            if user_input.lower() in ["quit", "exit", "close"]:
                print("\n👋 Goodbye! Your conversation has been saved.")
                save_chat_history(conversation_history)
                break
            
            if user_input.lower() == "history":
                print("\n📜 Conversation History:")
                print("=" * 70)
                for i, msg in enumerate(conversation_history, 1):
                    role = msg["role"].upper()
                    content = msg["content"][:100] + "..." if len(msg["content"]) > 100 else msg["content"]
                    print(f"{i}. [{role}]: {content}")
                print("=" * 70)
                continue
            
            if user_input.lower() == "clear":
                conversation_history = []
                save_chat_history(conversation_history)
                print("🗑️  Conversation history cleared.")
                continue
            
            # Run the agent with the user input
            conversation_history = run_agent(user_input, conversation_history)
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Session interrupted by user.")
            save_chat_history(conversation_history)
            break
        except Exception as e:
            print(f"\n❌ Error in conversation loop: {str(e)}")
            import traceback
            traceback.print_exc()
            continue


# ============================================================================
# 7. MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    interactive_session()

    '''print("🔒 Secure connection established with NVIDIA NIM!")
    print("📝 Advanced Note-Taking Agent Started\n")
    
    history = None
    
    # Test scenarios demonstrating all features
    test_prompts = [
        "Please take a note: Code is running perfectly inside GitHub Codespaces.",
        "What are my current notes?",
        "Add another note: Testing tool execution and multi-turn conversation successfully.",
        "Search my notes for 'GitHub'",
        "Can you save a note about Python learning progress?",
        "Export my notes as JSON",
        "Show me all my notes again"
    ]
    
    print("Running comprehensive test suite...\n")
    
    for prompt in test_prompts:
        history = run_agent(prompt, history)
        print()
'''
